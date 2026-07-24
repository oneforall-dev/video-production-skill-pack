---
name: caption-designer
description: Diseña subtítulos dinámicos desde timestamps por palabra, con bloques legibles, énfasis selectivo, presets de marca y safe zones para formatos sociales. Usar para crear captions quemados o composiciones de subtítulos para Reels, TikTok, Shorts, podcasts y video corporativo.
---

# Diseñar captions

Optimizar lectura, sincronía y jerarquía; no convertir cada palabra en un efecto.

## Flujo

1. Leer transcript por palabra, formato de entrega y brand profile.
2. Agrupar en bloques de 2–7 palabras, máximo dos líneas y una unidad semántica por bloque.
3. Evitar dejar artículos/preposiciones aislados. Dividir en pausas naturales y cambios de speaker.
4. Resaltar como máximo una palabra o frase corta por bloque cuando aporte comprensión.
5. Generar `data/caption-plan.json` con bloques, palabras, estilos, safe zone y fallback.
6. Validar colisiones con rostro, lower thirds, controles de plataforma y bordes.

## Presets

Soportar `minimal`, `hormozi`, `podcast`, `corporate`, `cinematic`, `kindness-is-cool` y `oneforall`. Tratar los presets como parámetros, no como copy fijo. Cargar colores, fuentes y logo desde `$brand-style-manager` cuando exista; nunca adivinar activos de marca.

## Accesibilidad

Mantener contraste suficiente, tamaño acorde a resolución y lectura mínima aproximada de 0,8 s salvo palabras muy breves. No usar solo color para indicar speaker o énfasis. Conservar SRT/VTT limpios además del diseño visual.
