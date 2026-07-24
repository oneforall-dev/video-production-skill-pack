---
name: edit-planner
description: Convierte transcripciones, análisis de talking head, objetivos, marca y plataforma en un edit-plan.json ejecutable sin renderizar. Usar para decidir cortes, captions, overlays, zooms, B-roll, música y efectos antes de Remotion o FFmpeg.
---

# Planificar edición

Generar una única fuente de verdad ejecutable y versionable. No modificar medios.

## Entradas

Exigir `metadata.json` y al menos transcript o instrucciones temporales. Incorporar, si existen, análisis talking-head, brand profile, formato social, B-roll, motion y audio.

## Salida

Escribir `data/edit-plan.json` con:

```json
{"schemaVersion":"1.0","sourceId":"","timebase":{"unit":"seconds","fps":30},"timeline":{"duration":0},"cuts":[],"captions":[],"overlays":[],"zooms":[],"reframes":[],"broll":[],"music":[],"soundEffects":[],"transitions":[],"deliverables":[],"warnings":[]}
```

Cada evento debe tener `id`, rango temporal válido, `source`, `reason`, `confidence` y parámetros específicos. Los IDs nunca cambian entre revisiones si la intención del evento sigue siendo la misma.

## Reglas

1. Resolver conflictos por prioridad: significado y voz, continuidad, legibilidad, marca, ritmo, decoración.
2. Mantener cortes y eventos ordenados, sin solapamientos ilegales.
3. No animar cada frase ni usar B-roll para cubrir contenido sin relación.
4. Separar tiempo de fuente (`sourceStart/sourceEnd`) de tiempo de salida (`start/end`).
5. Registrar decisiones omitidas como warnings, no como valores inventados.
6. Validar contra `references/edit-plan.schema.json` si está disponible.

Entregar el plan a `$remotion-composer`, `$ffmpeg-renderer`, `$video-reviewer` y `$version-manager`.
