---
name: social-format-adapter
description: Adapta una edición a TikTok, Reels, Shorts, Stories, YouTube 16:9, LinkedIn 1:1 y otros formatos, reencuadrando contenido, captions y composición por plataforma. Usar para generar entregables derivados sin simplemente recortar el master.
---

# Adaptar formatos sociales

Diseñar cada variante para su superficie y conservar una narrativa coherente.

## Flujo

1. Leer master plan, transcript, brand profile y plataformas solicitadas.
2. Crear un deliverable por combinación real de plataforma/aspecto; no duplicar archivos idénticos con nombres distintos.
3. Reencuadrar con seguimiento de sujeto y keyframes revisables. Usar layout alternativo cuando un crop destruya contexto.
4. Refluir captions, lower thirds, CTA y B-roll según safe zones de la plataforma.
5. Ajustar hook, ritmo y duración solo si el usuario autoriza una versión editorial distinta.
6. Escribir `data/format-plan.json` con resolución, FPS, aspect, safe zones, crop/reframe, caption overrides y export settings.

## Calidad

Validar 9:16, 1:1 y 16:9 por separado. No asumir que TikTok y Reels tienen overlays idénticos; mantener safe zones configurables y fechadas. Pasar entregables a `$edit-planner`.
