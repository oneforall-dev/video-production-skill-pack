---
name: highlight-extractor
description: Encuentra y puntúa fragmentos autocontenidos de videos largos usando hooks, ideas completas, consejos, tensión, emoción, CTA y duración. Usar para proponer 5–10 clips derivados de entrevistas, podcasts, webinars, cursos o grabaciones extensas.
---

# Extraer highlights

Buscar fragmentos con apertura, desarrollo y cierre; no seleccionar frases aisladas solo por sonar intensas.

## Flujo

1. Leer transcript, speakers, escenas y objetivo de audiencia.
2. Generar candidatos en límites de frase/idea con handles editables.
3. Puntuar `hook`, `completeness`, `specificity`, `emotion`, `novelty`, `standaloneClarity`, `ctaFit` y `durationFit`.
4. Penalizar dependencia de contexto, repetición entre clips, afirmaciones dudosas y comienzos lentos.
5. Seleccionar un conjunto diverso; evitar que los clips repitan la misma idea o apertura visual.
6. Escribir `data/highlights.json` con rango fuente, título, hook, resumen, score desglosado, contexto requerido y sugerencias de formato/B-roll.

## Integridad

No fabricar polémica ni cambiar la intención mediante cortes. Marcar fragmentos sensibles para revisión humana. Pasar los candidatos elegidos a `$edit-planner` y `$social-format-adapter`.
