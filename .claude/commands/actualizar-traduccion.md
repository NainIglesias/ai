---
description: Trae los cambios del repositorio del profesor (avidaldo/ai) a traduccion-es y los traduce al español
---

Actualiza la traducción al español de este repositorio con los cambios nuevos del original, avidaldo/ai. Antes de empezar, lee `tools/traduccion/GLOSARIO.md`: tiene las convenciones y los términos, y hay que seguirlos al pie de la letra.

## 1. Ver qué falta

```bash
git fetch upstream            # si no existe: git remote add upstream https://github.com/avidaldo/ai
git checkout traduccion-es && git pull --ff-only origin traduccion-es
tools/traduccion/pendiente.sh
```

Si no sale nada, la traducción está al día: dilo y termina. Si hay cambios, enséñame los commits (`git log --oneline REF..upstream/main`) y el número de ficheros afectados, y sigue.

## 2. Merge en una rama nueva

```bash
git checkout -b actualiza-<sha corto de upstream/main>
git merge upstream/main --no-commit
```

Resuelve los conflictos así: **se conserva nuestra traducción y se aplica en español lo que haya cambiado upstream**. Para ver qué cambió exactamente en un fichero: `git diff REF upstream/main -- <fichero>`. Haz commit del merge con el mensaje `Merge upstream avidaldo/ai hasta <sha corto>`.

## 3. Traducir cada fichero añadido o modificado

- **Ficheros nuevos (A)**: tradúcelos enteros.
- **Ficheros modificados (M)**: traduce solo lo que ha cambiado. No reescribas ni "mejores" lo que ya está en español: si un párrafo traducido cambia en upstream, modifica solo las frases o cifras que cambiaron y conserva la redacción.
- **Renombrados o borrados (R, D)**: arregla los enlaces que apunten a ellos.
- **`requirements.txt`, `.gitignore` y la configuración**: la versión de upstream, sin traducir.

Para cada notebook:
1. `python tools/traduccion/nbtr.py extract NB.ipynb <scratchpad>/NN.en.txt`
2. Escribe `<scratchpad>/NN.es.txt`:
   - con los mismos marcadores `@@` y en el mismo orden;
   - traduciendo solo el texto;
   - en los segmentos de código (`@@ c:l`), solo el comentario, conservando el `#` inicial.
3. `python tools/traduccion/nbtr.py apply NB.ipynb <scratchpad>/NN.es.txt`

Los docstrings no los extrae nbtr.py, así que se traducen editando el notebook directamente. En los notebooks modificados, compara con la versión traducida anterior (`git show HEAD~1:NB.ipynb`, antes del merge) para reutilizar lo que ya estaba traducido y no traducirlo de otra forma.

Si un encabezado cambia, actualiza los anclajes que apuntan a él en todo el repositorio.

## 4. Actualizar la referencia y comprobar

- En `README.md`, cambia el sha de «hasta el commit …» por el sha **completo** de `upstream/main`.
- Si upstream cambió el README raíz, tradúcelo también.
- Ejecuta `python tools/traduccion/check.py` y corrige hasta que diga `0 problema(s)`.
- Vuelve a ejecutar `tools/traduccion/pendiente.sh`: ahora debe salir vacío.

## 5. Commit e integración

Haz commits con mensajes en español: uno por carpeta grande, o uno solo si el cambio es pequeño. Después **pregúntame** antes de:
- hacer fast-forward de `traduccion-es` a esta rama y `git push origin traduccion-es`;
- actualizar `main` (`git checkout main && git merge --ff-only upstream/main && git push origin main`, sin traducir nada);
- cerrar el issue «Traducción pendiente» del fork, si está abierto (`gh issue close ... -R NainIglesias/ai`).

$ARGUMENTS
