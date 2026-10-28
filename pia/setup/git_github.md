# Git y GitHub: de los commits a los pull requests

## Git: la historia de un proyecto

**Git** registra la historia de un proyecto. Un **repositorio** es una carpeta de proyecto cuya historia guarda Git, en una carpeta oculta `.git`. Un **commit** es una instantánea del proyecto en un momento dado, con un mensaje que dice qué cambió y por qué, y un puntero al commit anterior. La historia es la cadena de commits.

```bash
git init                     # convierte la carpeta actual en un repositorio
git status                   # qué ha cambiado desde el último commit
git add notebook.ipynb       # elige los cambios para el próximo commit (el área de preparación o staging)
git commit -m "Add the first models"
git log --oneline            # la historia, un commit por línea
```

Antes de tu primer commit, dile a Git quién eres. El nombre y el email se escriben en cada commit, y se hacen públicos cuando publicas uno. GitHub da a cada cuenta una dirección privada, `ID+usuario@users.noreply.github.com`, que puedes encontrar en su configuración de email y usar en lugar de la tuya:

```bash
git config --global user.name "Tu nombre o usuario"
git config --global user.email "ID+usuario@users.noreply.github.com"
```

## Lo que nunca hay que subir: `.gitignore`

Un archivo `.gitignore` en la raíz del repositorio lista los archivos que Git debe dejar fuera, un patrón por línea. En un proyecto de Python para IA, esto nunca debe ir en Git:

```text
# El entorno virtual: cualquiera puede recrearlo a partir de requirements.txt
.venv/
# Los archivos compilados de Python
__pycache__/
# Secretos, como claves de API
.env
# Datasets: los descarga el código, no se suben
data/
# Pesos de modelos: pesan mucho y se pueden reproducir entrenando
*.pt
*.pth
```

En un `.gitignore`, `#` solo empieza un comentario al principio de una línea, y por eso cada comentario va en su propia línea.

`.gitignore` solo afecta a archivos que todavía no están siendo seguidos. Para dejar de seguir un archivo que subiste por error, manteniéndolo en el disco: `git rm --cached archivo`. Un secreto que se haya subido alguna vez debe considerarse público: revócalo y crea uno nuevo.

## Deshacer cosas

```bash
git restore notebook.ipynb          # descarta los cambios sin commit de un archivo
git restore --staged notebook.ipynb # saca un archivo del área de preparación, conservando sus cambios
git commit --amend                  # rehace el último commit (su mensaje, o un archivo olvidado): solo antes de hacer push
git revert <commit>                 # un commit nuevo que deshace uno antiguo: la forma segura una vez hecho push
```

## Ramas

Una **rama** es un nombre móvil para una línea de commits. La línea principal suele llamarse `main` (los repositorios más antiguos usan `master`). Trabajar en una rama mantiene un cambio sin terminar separado de `main` hasta que esté listo:

```bash
git switch -c fix-typo       # crea la rama fix-typo y cámbiate a ella
# edita, haz add y commit como siempre
git switch main              # vuelve a main
git merge fix-typo           # trae los commits de la rama a main
```

## Remotos: tu máquina y la forja

Un **remoto** es otra copia del repositorio, normalmente en una **forja**: un servicio que aloja repositorios en línea, como GitHub, GitLab o Codeberg. El remoto desde el que clonaste se llama `origin`.

```bash
git clone https://github.com/OWNER/REPO.git   # copia un repositorio a tu máquina, con origin configurado
git push                                     # envía tus commits nuevos a origin
git pull                                     # trae los commits nuevos de origin a tu rama
```

Para hacer push a GitHub tienes que autenticarte. La forma más sencilla es la [CLI de GitHub](https://cli.github.com/): ejecuta `gh auth login` una vez, y Git usa ese inicio de sesión. Las claves SSH son la otra forma habitual.

## ¿Clonar o hacer fork?

- **Clonar:** una copia de un repositorio en tu máquina. Siempre puedes clonar un repositorio público, pero solo puedes hacer push si su propietario te deja.
- **Fork:** una copia de un repositorio en la forja, bajo tu propia cuenta. Puedes hacer push a tu fork, así que un fork es la forma de trabajar en un repositorio que no es tuyo: haz fork en la forja y después clona tu fork.

Un fork recuerda de dónde viene. El repositorio original se llama **upstream**.

## Issues

Una **issue** es una conversación pública y numerada en un repositorio sobre una sola cosa: un error, una pregunta, una propuesta o una tarea. Las issues tienen un título, una descripción, comentarios, **etiquetas** que las clasifican (`bug`, `good first issue`…) y a veces una persona asignada.

En cualquier parte de GitHub, `#12` enlaza con la issue 12 del mismo repositorio. Un pull request cuya descripción dice `Closes #12` cierra esa issue cuando se fusiona en la rama por defecto.

## Contribuir con un pull request

Un **pull request** (un *merge request* en GitLab) propone los commits de una de tus ramas a un repositorio en el que no puedes hacer push. Sus propietarios lo revisan, comentan y lo fusionan, o no.

1. **Haz fork** del repositorio en GitHub (el botón *Fork*) y clona tu fork.
2. **Crea una rama** para el cambio: `git switch -c better-explanation`.
3. **Haz commit** de tu cambio, en uno o pocos commits con mensajes claros.
4. **Sube la rama a tu fork:** `git push -u origin better-explanation`.
5. **Abre el pull request.** GitHub te lo ofrece en cuanto haces push; si no, usa la pestaña *Pull requests* de tu fork. Comprueba que va de la rama de tu fork a la `main` del repositorio original. Di qué cambiaste y por qué, y enlaza la issue que resuelve.
6. **Responde a la revisión.** Los commits nuevos que subas a la misma rama se añaden al pull request, así que arreglas en esa rama lo que pida la revisión.
7. **Después de la fusión,** borra la rama y actualiza tu fork (siguiente sección).

Nunca trabajes directamente en la `main` de tu fork: mantén cada cambio en una rama, para que `main` siempre pueda seguir a upstream.

## Mantener tu fork al día

Un fork no se actualiza solo: cuando upstream recibe commits nuevos, tu fork se queda donde estaba. En los repositorios de los proyectos esto pasa en cada paso, porque la solución de cada paso llega a upstream.

La forma más sencilla es el botón **Sync fork** de GitHub, en la página de tu fork, seguido de `git pull` en tu máquina. Desde la línea de comandos:

```bash
git remote add upstream https://github.com/OWNER/REPO.git   # una vez por clon
git switch main
git fetch upstream                                           # descarga los commits nuevos de upstream
git merge upstream/main                                      # incorpóralos a tu main
git push origin main                                         # actualiza tu fork en GitHub
```

Después empieza la siguiente rama desde la `main` actualizada. Si mantuviste tu trabajo en ramas, la fusión en `main` es un *fast-forward*: no puede haber conflictos. Para traer los commits nuevos a una rama en la que todavía estás trabajando, fusiona `main` en ella (`git merge main` desde esa rama) y resuelve los conflictos que haya.

## Hacer pull después de ejecutar notebooks

Ejecutar un notebook cambia su archivo: las salidas y los contadores de ejecución se guardan dentro. Si un notebook que ejecutaste también se actualizó en upstream, `git pull` se detiene en lugar de sobrescribir tus cambios. Decide cuánto vale tu copia:

```bash
git status                     # qué archivos cambiaste
git restore notebook.ipynb     # descarta tu ejecución y después haz pull
git stash                      # o aparta tus cambios,
git pull                       # haz pull,
git stash pop                  # y recupéralos (Git te pide que resuelvas los conflictos)
```

Para evitar el problema, haz tus propios experimentos en una copia del notebook, o en una rama de tu fork, y ejecuta el original solo para leerlo.

## Tags: versiones con nombre

Un **tag** es un nombre fijo para un commit, como `v0.3`. A diferencia de una rama, nunca se mueve, así que da nombre a una versión del proyecto para siempre. Los repositorios de los proyectos etiquetan cada versión, y cada examen trabaja sobre un tag.

```bash
git fetch upstream --tags            # descarga los tags de upstream
git tag                              # lístalos
git switch --detach v0.3             # mira el proyecto tal como estaba en v0.3
git switch main                      # vuelve
git switch -c my-changes v0.3        # o empieza una rama desde él, para cambiar cosas
```

## Otras formas de hacer lo mismo

Todo lo anterior también se puede hacer desde un editor (el panel *Source Control* de VS Code), desde las páginas web de GitHub o con la CLI de GitHub: `gh repo fork OWNER/REPO --clone` hace fork y clona en un solo paso, con `upstream` ya configurado, y `gh pr create` abre un pull request desde la rama actual. Uses lo que uses, ejecuta las mismas operaciones de Git.

## Más recursos

- [Pro Git](https://git-scm.com/book/es/v2), el libro oficial, gratis en línea (también en español).
- [Learn Git Branching](https://learngitbranching.js.org/?locale=es_ES): un juego interactivo para practicar ramas, fusiones y *rebases*.
- [Recursos de Git y GitHub](https://github.com/avidaldo/recursos-git) (en español): cursos, vídeos y tutoriales.
