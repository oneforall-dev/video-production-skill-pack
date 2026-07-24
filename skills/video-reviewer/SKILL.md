---
name: video-reviewer
description: Realiza control de calidad técnico y editorial sobre renders de video, detectando frames negros, cortes, captions fuera de zona, desincronización, audio problemático, silencios, texto cortado y especificaciones incorrectas. Usar antes de entregar o aprobar una versión.
---

# Revisar video

Combinar mediciones automáticas con muestreo visual y auditivo. No aprobar basándose solo en que el archivo abre.

## Controles

- ffprobe: codec, resolución, FPS, duración, canales, sample rate y pix_fmt.
- Señal: blackdetect, freezedetect, silencedetect, ebur128/volumedetect y clipping.
- Timeline: duración esperada, cortes, transiciones, audio continuo y sincronía.
- Diseño: captions, overlays, safe zones, contraste, colisiones y texto truncado.
- Contenido: inicio/final accidentales, CTA completo y frames de placeholder.

## Salida

Escribir `data/review-report.json`:

```json
{"status":"changes_required","renderId":"","summary":"","checks":[],"issues":[{"id":"issue-001","time":14.2,"end":14.8,"severity":"major","type":"caption_overflow","evidence":"","instruction":"Reducir el tamaño del caption un 10%."}]}
```

Usar estados `passed`, `passed_with_warnings` o `changes_required`; severidades `critical`, `major`, `minor`. Cada issue debe ser accionable y temporalmente localizable. No afirmar que un chequeo visual pasó si no se renderizó/inspeccionó.

Enviar issues a `$revision-interpreter`.
