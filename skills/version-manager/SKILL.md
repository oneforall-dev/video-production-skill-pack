---
name: version-manager
description: Gestiona versiones inmutables de planes, renders, revisiones y comentarios de proyectos de video. Usar al crear v001/v002, comparar ediciones, volver a una versión, registrar cambios o actualizar current sin sobrescribir entregables anteriores.
---

# Gestionar versiones

Tratar cada render aprobado o revisable como inmutable.

## Estructura

Usar `versions/v001/` para plan, manifiesto, comentarios y review; `renders/v001.<ext>` para el medio. `renders/current.<ext>` es una copia o enlace conveniente, nunca la única copia.

## Flujo

1. Bloquear el manifiesto durante la asignación de número para evitar colisiones.
2. Calcular el siguiente `vNNN`; no reutilizar números eliminados.
3. Copiar plan y artefactos de control a la carpeta de versión.
4. Escribir `data/versions.json` de forma atómica con parent, hashes, autor, fecha, cambios, comentarios y estado.
5. Actualizar `current` solo después de verificar el hash del nuevo render.
6. Para rollback, crear una versión nueva basada en la anterior; no reescribir la historia.
7. Comparar planes por IDs estables y reportar altas, bajas y cambios de parámetros.

## Estados

Usar `draft`, `review`, `changes_required`, `approved` y `delivered`. Nunca marcar `approved` sin evidencia de revisión. No comprimir ni publicar sin confirmación explícita.
