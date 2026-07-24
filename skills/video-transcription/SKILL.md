---
name: video-transcription
description: Transcribe audio o video con timestamps por palabra, segmentos legibles, idioma y diarización opcional, exportando JSON, SRT y VTT. Usar cuando una edición, subtitulado, búsqueda de highlights o análisis de voz requiera una transcripción temporal verificable.
---

# Transcribir video

Crear una fuente temporal canónica; no corregir silenciosamente el significado del hablante.

## Flujo

1. Leer `metadata.json` y usar WAV 48 kHz cuando exista.
2. Elegir motor por disponibilidad y privacidad: Faster Whisper local, Whisper local o API autorizada. Registrar motor, modelo, idioma solicitado/detectado y parámetros.
3. Solicitar timestamps por palabra. Activar diarización solo si hay evidencia de múltiples voces y el motor la soporta.
4. Normalizar cada palabra a `{id,text,start,end,confidence,speaker}`. Mantener `start >= 0`, `end > start` y orden monotónico.
5. Agrupar palabras en frases por puntuación, cambio de speaker, pausa y longitud; no derivar los segmentos primero y adivinar después los tiempos de palabra.
6. Exportar `data/transcript.json`, `captions/transcript.srt` y `captions/transcript.vtt`.
7. Marcar pasajes de baja confianza y palabras inaudibles. No inventar texto.

## Contrato

Incluir `schemaVersion`, `sourceId`, `language`, `languageConfidence`, `duration`, `speakers`, `words`, `segments`, `engine` y `warnings`. Los tiempos se expresan en segundos. SRT usa coma y VTT punto para milisegundos.

Pasar `transcript.json` a `$talking-head-editor`, `$edit-planner`, `$caption-designer` o `$highlight-extractor`.
