---
name: revision-interpreter
description: Convierte comentarios humanos de revisión en operaciones técnicas estructuradas contra IDs y tiempos de un edit-plan. Usar cuando el usuario pide quitar pausas, cambiar textos, ajustar volumen, reemplazar B-roll, modificar estilos o aplicar feedback sin operar una timeline manual.
---

# Interpretar revisiones

Traducir intención sin ejecutar cambios ambiguos.

## Flujo

1. Leer comentario, versión objetivo, edit-plan, review report y elementos visibles.
2. Resolver referencias como “aquí”, “este texto” o “la segunda toma” usando playhead, timecode, issue ID u overlay ID disponible.
3. Si hay varias coincidencias materiales, devolver `needs_clarification` con candidatos; no elegir al azar.
4. Emitir operaciones idempotentes en `data/revision-operations.json`.
5. Validar que rangos existan, IDs estén presentes y parámetros sean compatibles.

## Operaciones

Soportar `remove_range`, `restore_range`, `trim_range`, `update_overlay`, `move_overlay`, `replace_asset`, `adjust_audio`, `update_caption_style`, `update_reframe`, `add_broll`, `remove_event` y `change_deliverable`.

Cada operación incluye `id`, `action`, `targetId`, `start/end` cuando aplique, `params`, `sourceComment`, `confidence` y `requiresReview`.

## Regla de seguridad

No traducir “hazlo mejor” a cambios arbitrarios. No mutar el plan original: generar un patch y pasarlo a `$version-manager` para crear una nueva revisión.
