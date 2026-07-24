---
name: motion-graphics-director
description: Decide dónde y cómo usar texto cinético, callouts, flechas, gráficos, screenshots animados, comparaciones y UI mockups en un video. Usar para convertir puntos clave en motion graphics con moderación antes de componer en Remotion.
---

# Dirigir motion graphics

Animar decisiones, no cada frase.

## Selección

Asignar motion solo a hooks, cambios de sección, cifras verificadas, comparaciones, pasos, conceptos difíciles o CTA. Mantener respiración visual entre eventos.

## Salida

Crear `data/motion-plan.json` con eventos que incluyan `id`, rango, `type`, `message`, `visualMechanic`, `entrance`, `hold`, `exit`, `priority`, `safeZone`, `brandTokens` y `reducedMotionFallback`.

## Reglas

- Elegir una mecánica dominante por segmento.
- No superponer gráficos sobre rostro, captions o controles.
- No inventar cifras ni recrear interfaces de terceros como si fueran propias.
- Usar easing y duración coherentes con el tono.
- Tratar screenshots como evidencia: conservar legibilidad y contexto.

Pasar el plan a `$edit-planner` y `$remotion-composer`.
