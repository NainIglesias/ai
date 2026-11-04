"""Comprueba la traducción frente al commit de upstream indicado en el README.

  python tools/traduccion/check.py [REF]

1. Cada notebook traducido tiene el mismo código (sin comentarios) y las mismas
   salidas que su versión en REF (por defecto, el commit citado en el README).
2. Ningún enlace interno (.md / .ipynb) apunta a un fichero o anclaje que no existe.

Sale con código 1 si encuentra algún problema.
"""
import json, os, re, subprocess, sys, unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from nbtr import comment_pos  # noqa: E402

ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
os.chdir(ROOT)


def readme_ref():
    m = re.search(r"hasta el commit ([0-9a-f]{7,40})", (ROOT / "README.md").read_text(encoding="utf-8"))
    if not m:
        sys.exit("No encuentro 'hasta el commit <sha>' en README.md")
    return m.group(1)


DOCSTRING = re.compile(r"^[ \t]*(\"\"\"|''')[\s\S]*?\1", re.M)


def strip_comments(src):
    """Quita comentarios y docstrings (lo único traducible dentro del código)."""
    src = DOCSTRING.sub("", src)
    out = []
    for line in src.split("\n"):
        p = comment_pos(line)
        out.append((line[:p] if p >= 0 else line).rstrip())
    return "\n".join(l for l in out if l)


def code_and_outputs(nb):
    return [(strip_comments("".join(c["source"])), c.get("outputs"))
            for c in nb["cells"] if c["cell_type"] == "code"]


def check_notebooks(ref):
    errors = []
    tracked = subprocess.check_output(["git", "ls-files", "*.ipynb"], text=True).split()
    for path in tracked:
        try:
            orig = subprocess.check_output(["git", "show", f"{ref}:{path}"], text=True,
                                           stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError:
            continue  # no existe en upstream
        a = code_and_outputs(json.loads(orig))
        b = code_and_outputs(json.loads(Path(path).read_text(encoding="utf-8")))
        if len(a) != len(b):
            errors.append(f"{path}: {len(b)} celdas de código, upstream tiene {len(a)}")
            continue
        for i, ((ca, oa), (cb, ob)) in enumerate(zip(a, b)):
            if ca != cb:
                errors.append(f"{path}: celda de código {i} distinta de upstream")
            elif oa != ob:
                errors.append(f"{path}: salidas de la celda de código {i} distintas de upstream")
    return errors


# ---------- anclajes ----------

def slug(heading):
    s = re.sub(r"<[^>]+>", "", heading)
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)  # enlaces -> texto
    s = s.strip().lower()
    s = "".join(ch for ch in s if ch in " -_" or unicodedata.category(ch)[0] in "LN")
    return s.replace(" ", "-")


def markdown_text(path):
    if path.suffix == ".ipynb":
        nb = json.loads(path.read_text(encoding="utf-8"))
        return "\n".join("".join(c["source"]) for c in nb["cells"] if c["cell_type"] == "markdown")
    return path.read_text(encoding="utf-8")


_anchor_cache = {}


def anchors(path):
    if path not in _anchor_cache:
        seen, result = {}, set()
        in_code = False
        for line in markdown_text(path).split("\n"):
            if line.lstrip().startswith("```"):
                in_code = not in_code
            if in_code:
                continue
            m = re.match(r"#{1,6}\s+(.*?)\s*#*\s*$", line)
            if m:
                s = slug(m.group(1))
                n = seen.get(s, 0)
                seen[s] = n + 1
                result.add(s if n == 0 else f"{s}-{n}")
        result |= set(re.findall(r'<a\s+(?:name|id)="([^"]+)"', markdown_text(path)))
        _anchor_cache[path] = result
    return _anchor_cache[path]


LINK = re.compile(r"\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def check_links():
    errors = []
    files = subprocess.check_output(["git", "ls-files", "*.md", "*.ipynb"], text=True).split()
    for f in files:
        src = Path(f)
        for target in LINK.findall(markdown_text(src)):
            if re.match(r"[a-z]+:", target):
                continue  # http:, mailto:, ...
            file_part, _, frag = target.partition("#")
            dest = (src.parent / file_part).resolve() if file_part else src.resolve()
            if not dest.exists():
                errors.append(f"{f}: enlace roto -> {target}")
                continue
            if frag and dest.suffix in (".md", ".ipynb") and frag not in anchors(dest):
                errors.append(f"{f}: anclaje inexistente -> {target}")
    return errors


def main():
    ref = sys.argv[1] if len(sys.argv) > 1 else readme_ref()
    errors = check_notebooks(ref) + check_links()
    for e in errors:
        print(e)
    print(f"{len(errors)} problema(s) (referencia upstream: {ref[:12]})")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
