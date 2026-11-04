# Cómo se mantiene al día la traducción

La rama `traduccion-es` de este fork es la traducción al español de [avidaldo/ai](https://github.com/avidaldo/ai). Mantenerla al día está automatizado: cada día se comprueba si el repositorio original ha cambiado y, si ha cambiado, Claude Code traduce los cambios y abre un pull request. Ese pull request lo revisa y lo fusiona una persona.

## La idea

La pieza central es una línea del [README](../../README.md) que indica hasta qué commit del original está traducida la rama:

> … hasta el commit `2c756c544bdb288bf3e3edc502d13a54e43e080d` …

Todo lo demás se apoya en esa referencia:
- Lo pendiente es lo que ha cambiado entre ese commit y el `main` actual del original (`git diff <commit> upstream/main`).
- Cuando una actualización termina, el commit del README pasa a ser el último del original.

## Las ramas

| Rama | Contenido |
| --- | --- |
| `main` | Copia exacta del `main` del profesor, sin traducir. Solo recibe sus cambios (`git merge --ff-only upstream/main`). |
| `traduccion-es` | La traducción. Es la rama por defecto del fork, y aquí viven las herramientas y el workflow. |
| `traduccion/<sha>` | Rama temporal que crea el workflow para cada actualización. Se convierte en un pull request contra `traduccion-es`. |

## Qué pasa cada día

El workflow [`.github/workflows/vigilar-upstream.yml`](../../.github/workflows/vigilar-upstream.yml) se ejecuta todos los días a las 07:17 UTC. También se puede lanzar a mano desde Actions → *Vigilar upstream* → *Run workflow*. Tiene dos jobs.

**1. `comprobar`** (gratis, unos segundos)
1. Descarga el `main` de avidaldo/ai.
2. Ejecuta `pendiente.sh`, que compara ese `main` con el commit del README.
3. Si coinciden, termina: la traducción está al día.
4. Si no coinciden, abre un issue *"Traducción pendiente: upstream tiene cambios"* con los commits nuevos y la lista de ficheros afectados. Si ese issue ya está abierto, lo actualiza en lugar de abrir otro.

**2. `traducir`** (solo si hay cambios)
1. **Antes de empezar comprueba dos cosas.** Si alguna falla, se salta este job y queda solo el issue:
   - que no haya ya un pull request de traducción esperando revisión;
   - que exista el secreto `CLAUDE_CODE_OAUTH_TOKEN`.
2. Crea la rama `traduccion/<sha>` y empieza el merge del original.
3. Lanza Claude Code con [`anthropics/claude-code-action`](https://github.com/anthropics/claude-code-action), usando la suscripción de Claude del dueño del fork (no la API de pago). Claude sigue las instrucciones de [`.claude/commands/actualizar-traduccion.md`](../../.claude/commands/actualizar-traduccion.md) y el [glosario](GLOSARIO.md):
   - resuelve los conflictos del merge;
   - traduce solo el texto nuevo o cambiado;
   - actualiza el commit del README;
   - hace commit.
4. Ejecuta `check.py`, sube la rama y abre un pull request.
   - La descripción lleva el resumen de Claude, con las decisiones dudosas que conviene revisar, y la línea "Closes #N", así que el issue se cierra al fusionar.
   - Si `check.py` encuentra problemas, el pull request se abre como borrador.
5. Si Claude falla (sin cuota en ese momento, token caducado…), no se sube nada. Se deja un comentario en el issue con el enlace a la ejecución, y se reintenta al día siguiente.

La revisión siempre la hace una persona: nada llega a `traduccion-es` sin fusionar el pull request.

## Las herramientas (`tools/traduccion/`)

| Fichero | Qué hace |
| --- | --- |
| `GLOSARIO.md` | Las convenciones de la traducción: qué se traduce y qué no, palabras que se quedan en inglés, tabla de términos, formato de números, anclajes. Es lo que lee Claude antes de traducir. |
| `pendiente.sh` | Lee el commit del README y lista los ficheros cambiados en el original desde entonces (`A` nuevo, `M` modificado, `D` borrado, `R` renombrado). No saca nada si está al día. |
| `nbtr.py` | Extrae lo traducible de un notebook a un fichero de texto y lo vuelve a aplicar sin tocar nada más. Lo traducible son las celdas markdown y los comentarios del código. |
| `check.py` | Detecta errores de traducción: código o salidas distintos del original, y enlaces o anclajes rotos. |

### `nbtr.py`

```bash
python3 tools/traduccion/nbtr.py extract notebook.ipynb en.txt   # notebook -> texto
# traducir en.txt y guardarlo como es.txt, manteniendo las líneas "@@ ..."
python3 tools/traduccion/nbtr.py apply   notebook.ipynb es.txt   # texto -> notebook
```

El fichero de texto se divide en segmentos:
- `@@ 5` es la celda markdown 5 entera;
- `@@ 7:3` es el comentario de la línea 3 de la celda de código 7.

`apply` falla si sobra o falta algún segmento. El código, las cadenas y las salidas no se tocan, y el JSON se escribe con el mismo formato que el original, así que el diff solo muestra el texto traducido.

### `check.py`

```bash
python3 tools/traduccion/check.py          # contra el commit del README
python3 tools/traduccion/check.py <sha>    # contra otro commit del original
```

Hace dos comprobaciones:
1. **Código y salidas.** Para cada notebook que existe en el original, el código, ignorando comentarios y docstrings (lo único que se traduce dentro del código), y las salidas deben ser idénticos.
2. **Enlaces.** Ningún enlace de un `.md` o `.ipynb` apunta a un fichero o un anclaje que no existe. Los anclajes se calculan como GitHub: en minúsculas, sin puntuación, con guiones y conservando las tildes.

Termina con `0 problema(s)` y código de salida 0 si todo está bien.

## Hacerlo a mano

Con [Claude Code](https://claude.com/claude-code) abierto en el repositorio:

```
/actualizar-traduccion
```

Hace lo mismo que el workflow (merge, traducción, README, `check.py`, commits) y pregunta antes de hacer push.

Sin Claude Code, los pasos son estos:

```bash
git fetch upstream
tools/traduccion/pendiente.sh                 # qué falta
git checkout -b actualiza traduccion-es
git merge upstream/main                       # resolver conflictos conservando la traducción
# traducir cada fichero de la lista (nbtr.py para los notebooks)
# cambiar el commit del README por el sha completo de upstream/main
python3 tools/traduccion/check.py             # debe dar 0 problemas
```

Para actualizar `main` (sin traducir):

```bash
git checkout main && git merge --ff-only upstream/main && git push origin main
```

## Configuración del fork

Hay que hacerla una sola vez:
- **Rama por defecto: `traduccion-es`.** GitHub solo ejecuta los workflows programados desde la rama por defecto.
- **Issues y Actions activados.** En un fork vienen desactivados.
- **Pull requests desde Actions.** Settings → Actions → General → *Allow GitHub Actions to create and approve pull requests*.
- **Secreto `CLAUDE_CODE_OAUTH_TOKEN`.** Se genera con `claude setup-token` y se guarda con `gh secret set CLAUDE_CODE_OAUTH_TOKEN -R NainIglesias/ai`. Si caduca, el workflow falla con `401 Invalid bearer token` y basta con repetir esos dos comandos.

## Coste

- Las GitHub Actions son gratis en repositorios públicos.
- La traducción consume cuota de la suscripción de Claude, no se paga aparte. Como referencia, la actualización de prueba de 21 notebooks con cambios pequeños tardó unos 2 minutos y 20 turnos.
- Si el repositorio pasa 60 días sin actividad, GitHub desactiva los workflows programados. Avisa por correo, y se reactivan con un clic en la pestaña Actions.

## Qué tocar para cambiar algo

| Quiero… | Fichero |
| --- | --- |
| Cambiar la frecuencia | `cron` en `vigilar-upstream.yml` ([sintaxis](https://crontab.guru)) |
| Cambiar cómo se traduce un término o el estilo | `GLOSARIO.md` |
| Cambiar los pasos que sigue Claude | `.claude/commands/actualizar-traduccion.md`, y el `prompt` de `vigilar-upstream.yml` para las diferencias en CI |
| Desactivar la traducción automática y quedarme solo con el aviso | Borrar el secreto `CLAUDE_CODE_OAUTH_TOKEN` |
| Pausarlo todo | Actions → *Vigilar upstream* → ⋯ → *Disable workflow* |
