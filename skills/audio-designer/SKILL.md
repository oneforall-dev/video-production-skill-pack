---
name: audio-designer
description: Diseña limpieza de voz, música, ducking, transiciones, efectos y loudness final para proyectos de video. Usar cuando se necesite un audio-plan reproducible para FFmpeg o Remotion sin saturar la mezcla con whooshes y hits.
---

# Diseñar audio

Hacer que la voz gobierne la mezcla.

## Flujo

1. Analizar ruido, hum, dinámica, sibilancia, clipping, room tone y loudness.
2. Proponer cadena conservadora de voz; no prometer reparar clipping irreversible.
3. Seleccionar música por función narrativa, licencia y energía, no por género genérico.
4. Definir ducking con ataque/release para evitar bombeo.
5. Añadir SFX solo a transiciones o acciones importantes; limitar repeticiones.
6. Crear `data/audio-plan.json` con tracks, rangos, gain, fades, sidechain, filtros, loudness target, true-peak ceiling y provenance.

## Targets

Tomar la plataforma como autoridad. Si no existe especificación, proponer un target y marcarlo como decisión pendiente; no afirmar un estándar universal. Pasar el plan a `$edit-planner` y `$ffmpeg-renderer`.
