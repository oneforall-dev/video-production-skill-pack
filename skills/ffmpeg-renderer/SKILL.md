---
name: ffmpeg-renderer
description: Ejecuta procesamiento audiovisual reproducible con FFmpeg/ffprobe: cortes, concatenación, proxies, limpieza y mezcla de audio, conversiones y renders finales con aceleración opcional. Usar cuando un edit-plan requiera procesamiento pesado o entrega codificada fuera de Remotion.
---

# Renderizar con FFmpeg

Construir comandos explícitos, registrarlos y verificar el resultado. No sobrescribir fuentes ni renders existentes.

## Flujo

1. Detectar versiones, encoders y hardware disponible. Elegir CPU como fallback seguro.
2. Traducir cortes del plan a filtros o segmentos con precisión de frame; evitar `-c copy` cuando los cortes no caigan en keyframes.
3. Procesar voz antes de música: reducción de ruido prudente, EQ si se justifica, compresión y loudness.
4. Aplicar ducking con sidechain cuando exista música. Evitar clipping y pumping.
5. Renderizar a un archivo temporal y moverlo atómicamente al destino versionado solo si FFmpeg termina correctamente.
6. Ejecutar ffprobe al resultado y escribir `data/render-report.json` con comando, duración, streams, tamaño, hash, encoder y warnings.

## Aceleración

Usar NVENC, VideoToolbox, QSV o VAAPI únicamente tras comprobar disponibilidad y compatibilidad de filtros/pixel format. Registrar el fallback.

## Límites

No usar `-y` sobre archivos finales. No interpolar texto no confiable en shell; pasar argumentos como lista o escapar de forma segura. Delegar el nombre de versión a `$version-manager` y QA a `$video-reviewer`.
