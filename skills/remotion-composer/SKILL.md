---
name: remotion-composer
description: Convierte edit-plan.json, caption-plan y brand profile en composiciones React de Remotion reutilizables. Usar para implementar captions animados, lower thirds, callouts, logos, progreso, B-roll, zooms y transiciones deterministas sin reescribir componentes en cada proyecto.
---

# Componer con Remotion

Usar Remotion para diseño temporal y composición, no para tareas pesadas que FFmpeg resuelve mejor.

## Arquitectura obligatoria

Crear o reutilizar `src/components/Captions.tsx`, `LowerThird.tsx`, `Callout.tsx`, `LogoReveal.tsx`, `ProgressBar.tsx` y `BrollFrame.tsx`. Separar datos del plan, tokens de marca y componentes. No generar JSX monolítico.

## Flujo

1. Validar el plan y derivar frames con redondeo consistente desde segundos.
2. Registrar composiciones por deliverable con resolución, FPS, duración y props validados.
3. Usar `Sequence`, `Series`, `Audio`, `Video` y componentes reutilizables. Mantener animaciones deterministas basadas en frame.
4. Implementar captions desde timestamps de palabra; no sincronizar con timers del navegador.
5. Aplicar zoom/reframe mediante transforms suaves y límites del plan.
6. Resolver activos con rutas portables y comprobar su existencia antes de renderizar.
7. Respetar safe zones, reducción de movimiento cuando corresponda y brand profile.

## Handoff

Exportar una composición reproducible y `data/composition-manifest.json`. Delegar preprocesado, normalización y transcodificación a `$ffmpeg-renderer`. No instalar paquetes ni cambiar versiones sin autorización.
