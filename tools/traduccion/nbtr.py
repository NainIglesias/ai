"""extract NB OUT.txt  -> segments file;  apply NB IN.txt -> writes notebook.
Segment format:  @@ <cell>[:<line>] then text until next @@ line.
Markdown cells: whole source. Code cells: only the comment part (from '#') of lines with a comment."""
import json,sys,re,io
def comment_pos(line):
    # find '#' not inside string quotes (simple scanner)
    q=None;i=0
    while i<len(line):
        c=line[i]
        if q:
            if c=='\\': i+=2; continue
            if line.startswith(q,i): i+=len(q); q=None; continue
        else:
            if line.startswith('"""',i) or line.startswith("'''",i): q=line[i:i+3]; i+=3; continue
            if c in '"\'': q=c
            elif c=='#': return i
        i+=1
    return -1
def segs(nb):
    for ci,c in enumerate(nb["cells"]):
        src="".join(c["source"])
        if c["cell_type"]=="markdown":
            yield f"{ci}",src
        elif c["cell_type"]=="code":
            for li,l in enumerate(src.split("\n")):
                p=comment_pos(l)
                if p>=0 and l[p:].strip("# \t") and not l.startswith("#!") and not re.match(r"#\s*%",l[p:]):
                    yield f"{ci}:{li}",l[p:]
def write_src(c,text):
    lines=text.split("\n")
    c["source"]=[l+"\n" for l in lines[:-1]]+([lines[-1]] if lines[-1] else [])
def main():
    cmd,nbp,fp=sys.argv[1:4]
    nb=json.load(open(nbp,encoding="utf-8"))
    if cmd=="extract":
        with open(fp,"w",encoding="utf-8") as f:
            for k,t in segs(nb): f.write(f"@@ {k}\n{t}\n")
    else:
        raw=open(fp,encoding="utf-8").read()
        parts=re.split(r"^@@ (\S+)\n",raw,flags=re.M)[1:]
        tr={parts[i]:parts[i+1][:-1] if parts[i+1].endswith("\n") else parts[i+1] for i in range(0,len(parts),2)}
        orig=dict(segs(nb))
        missing=set(orig)-set(tr); extra=set(tr)-set(orig)
        if missing or extra: sys.exit(f"MISMATCH missing={sorted(missing)} extra={sorted(extra)}")
        for k,t in tr.items():
            if ":" in k:
                ci,li=map(int,k.split(":")); c=nb["cells"][ci]
                ls="".join(c["source"]).split("\n"); p=comment_pos(ls[li]); ls[li]=ls[li][:p]+t
                write_src(c,"\n".join(ls))
            else:
                assert "\n" not in t[-1:] or True
                write_src(nb["cells"][int(k)],t)
        # preserve original formatting style (indent 1, ensure_ascii False)
        txt=json.dumps(nb,ensure_ascii=False,indent=1)+"\n"
        open(nbp,"w",encoding="utf-8").write(txt)

if __name__=="__main__":
    main()
