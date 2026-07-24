---
name: brand-style-manager
description: Crea y mantiene perfiles de marca reutilizables para edición de video, incluyendo fuentes, colores, captions, logos, motion, audio, safe zones y tono. Usar cuando un cliente como Oneforall, Kindness Is Cool o Prime Equity requiera consistencia entre videos.
---

# Gestionar estilo de marca

Extraer valores de fuentes reales y mantenerlos separados de los planes de edición.

## Flujo

1. Localizar guía, logo, fuentes, ejemplos y reglas proporcionadas.
2. Distinguir valores verificados, inferidos y pendientes. No adivinar colores o licencias.
3. Crear `brands/<slug>/brand-profile.json` con `schemaVersion`, identidad, typography, colors, captions, logo, motion, audio, imagery, safeZones y tone.
4. Copiar activos autorizados con hashes y licencia/procedencia; no incrustar secretos ni URLs temporales.
5. Definir fallbacks de fuentes y versiones monocromas del logo.
6. Versionar cambios del perfil; no alterar proyectos históricos automáticamente.

## Integridad

Validar contraste y disponibilidad de fuentes. Para Oneforall, usar el perfil real existente si se suministra; no asumir que una muestra antigua sigue vigente. Exponer tokens a `$caption-designer`, `$motion-graphics-director` y `$remotion-composer`.
