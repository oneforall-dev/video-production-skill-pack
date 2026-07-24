---
name: broll-director
description: Detecta frases que se benefician de apoyo visual y crea un plan de B-roll específico con stock, capturas, imágenes, diagramas, producto o generación autorizada. Usar para enriquecer talking heads y ocultar cortes sin cubrir todo el video ni inventar material.
---

# Dirigir B-roll

Usar B-roll cuando aclara, demuestra, contextualiza o resuelve continuidad; no como decoración automática.

## Flujo

1. Puntuar segmentos por necesidad visual, abstracción, demostrabilidad y valor narrativo.
2. Priorizar activos propios y capturas verificables; después stock; por último generación autorizada.
3. Describir cada plano con intención, contenido, encuadre, movimiento, duración, fuente y términos de búsqueda.
4. Evitar imágenes literales para cada sustantivo y repetir el mismo hook visual en una serie.
5. Generar `data/broll-plan.json` con IDs, rangos, `purpose`, `sourceType`, `brief`, `assetStatus`, `license`, `safeCrop` y fallback.
6. Marcar afirmaciones que no deben representarse como hechos si el medio es conceptual o generado.

Pasar el plan a `$edit-planner` y `$remotion-composer`.
