---
name: talking-head-editor
description: Analiza videos de una o varias personas hablando a cámara y propone cortes de errores, repeticiones y silencios, preservando pausas naturales, continuidad de audio y sentido. Usar para limpiar entrevistas, podcasts visuales, cursos, testimonios y talking-head antes de generar el plan de edición.
---

# Editar talking head

Tomar decisiones conservadoras y reversibles. Esta skill analiza y propone; no renderiza.

## Clasificar

Etiquetar rangos como `natural_pause`, `awkward_pause`, `mistake`, `repetition`, `restart`, `idea_change`, `breath` o `keep`. Usar transcripción, energía de audio y contexto visual juntos.

- Conservar pausas que separen ideas, respiraciones breves y silencios con intención emocional.
- Reducir pausas incómodas cuando rompan el ritmo, sin producir habla robótica.
- Eliminar errores solo si la toma siguiente completa la idea.
- Detectar repeticiones semánticas, no solo texto idéntico.
- No cortar en fonemas, respiraciones fuertes, parpadeos extremos o movimientos incompatibles.

## Flujo

1. Leer video, waveform, transcript y objetivo/plataforma.
2. Producir `data/talking-head-analysis.json` con rangos, evidencia, confianza y recomendación.
3. Construir `keepRanges` y `removeRanges` no solapados, con handles configurables.
4. Proponer jump cuts, punch-ins sutiles y reencuadres; limitar zooms a cambios de énfasis y ocultación de cortes.
5. Para 9:16, seguir rostro/ojos y validar safe zones; no centrar mecánicamente cada frame.
6. Preservar audio continuo con room tone y crossfades cortos.

## Límites

No eliminar afirmaciones, disclaimers o contexto que cambie el significado. Marcar ambigüedades para revisión humana. Pasar el análisis a `$edit-planner`.
