Video Production Skill Pack
Pack modular de 16 skills para analizar, planificar, componer, renderizar, revisar y versionar ediciones de video asistidas por Codex.

El sistema separa las decisiones editoriales del procesamiento audiovisual: Remotion controla la composición visual; FFmpeg se ocupa de cortes, audio y codificación; los planes JSON mantienen cada cambio reproducible y revisable.

Contenido
Flujo principal
Skill	Responsabilidad
video-ingestion	Validar el video, preservar el original y generar metadatos, audio, proxy y miniaturas.
video-transcription	Crear transcripción por palabras, segmentos, speakers, SRT y VTT.
talking-head-editor	Clasificar pausas, errores y repeticiones; proponer cortes y reencuadres.
edit-planner | Consolidar todas las decisiones en un edit-plan.json ejecutable.	
caption-designer	Diseñar captions sincronizados, legibles y seguros para cada plataforma.
remotion-composer	Convertir el plan en composiciones y componentes React reutilizables.
ffmpeg-renderer	Ejecutar cortes, mezcla, normalización, conversión y render pesado.
video-reviewer	Detectar problemas técnicos, editoriales, visuales y de audio.
revision-interpreter	Traducir comentarios humanos a operaciones técnicas sobre el plan.
version-manager	Crear versiones inmutables, comparar cambios y proteger renders previos.
Dirección creativa y adaptación
Skill	Responsabilidad
broll-director	Proponer B-roll útil, específico y con procedencia.
motion-graphics-director	Decidir dónde usar callouts, texto cinético, gráficos y UI animada.
audio-designer	Diseñar limpieza de voz, música, ducking, SFX y loudness.
brand-style-manager	Mantener perfiles reutilizables de marca y activos verificados.
social-format-adapter	Adaptar composición, captions y encuadre a cada plataforma.
highlight-extractor	Encontrar fragmentos autocontenidos para clips derivados.
Requisitos
Obligatorios
Python 3.10 o posterior para el instalador y los scripts incluidos.
Codex con soporte para skills.
Según el flujo utilizado
FFmpeg y ffprobe para ingesta, procesamiento, render y revisión técnica.
Node.js, React y Remotion para composiciones programáticas.
Whisper, Faster Whisper o una API autorizada para transcripción.
Aceleración NVENC, QSV, VAAPI o VideoToolbox opcional.
El pack no instala estas herramientas ni solicita credenciales. Cada skill comprueba la disponibilidad antes de usarlas y debe ofrecer un fallback seguro cuando corresponda.

Instalación
Descomprimir el paquete y ejecutar desde su carpeta raíz:

Copiar
python .\install.py
Por defecto, las skills se copian a:

$CODEX_HOME/skills, si CODEX_HOME está definido.
~/.codex/skills, en caso contrario.
Instalar en otra ubicación:

Copiar
python .\install.py --target "C:\ruta\a\skills"
Comprobar qué se instalaría sin copiar archivos:

Copiar
python .\install.py --dry-run
El instalador no sobrescribe skills existentes. Tras revisarlas, se puede autorizar el reemplazo explícito:

Copiar
python .\install.py --force
Validación
Validar el pack completo:

Copiar
python .\validate_pack.py
Validar un plan de edición:

Copiar
python .\skills\edit-planner\scripts\validate_edit_plan.py .\proyecto\data\edit-plan.json
Inspeccionar un video con ffprobe:

Copiar
python .\skills\video-ingestion\scripts\probe_media.py .\video.mp4 .\proyecto\data\metadata.json
Reservar la siguiente versión inmutable:

Copiar
python .\skills\version-manager\scripts\next_version.py .\proyecto --note "Primera revisión"
Flujo recomendado
Copiar
video-ingestion
  → video-transcription
  → talking-head-editor / highlight-extractor
  → brand-style-manager
  → broll-director / motion-graphics-director / audio-designer
  → social-format-adapter / caption-designer
  → edit-planner
  → remotion-composer / ffmpeg-renderer
  → video-reviewer
  → revision-interpreter
  → version-manager
No es obligatorio ejecutar todas las skills. Un subtitulado sencillo puede usar ingesta, transcripción y captions; un talking head completo puede recorrer todo el pipeline.

Ejemplos de uso
Invocar una skill de forma explícita:

Copiar
Usa $video-ingestion para preparar entrevista.mp4 y generar un proxy de edición.
Copiar
Usa $talking-head-editor para eliminar errores y pausas incómodas sin quitar respiraciones naturales.
Copiar
Usa $edit-planner para consolidar la transcripción, los captions y el B-roll en edit-plan.json.
Copiar
Usa $video-reviewer para revisar el render vertical y devolver issues con timecode e instrucciones accionables.
Copiar
Usa $revision-interpreter para convertir “quita la pausa después del segundo ejemplo” en un patch técnico.
Contratos y principios
Expresar tiempos internos en segundos decimales.
Diferenciar tiempo de fuente y tiempo de salida.
Mantener IDs estables entre revisiones.
Registrar procedencia, herramientas, modelos y warnings.
No inventar transcripciones, métricas, activos de marca ni resultados de QA.
No sobrescribir originales, planes históricos ni renders versionados.
Mantener captions, motion graphics y B-roll dentro de sus zonas de composición.
Solicitar revisión humana cuando una decisión pueda cambiar el significado.
Estructura
Copiar
video-production-skill-pack/
├── README.md
├── manifest.json
├── install.py
├── validate_pack.py
├── validation.json
└── skills/
    └── <skill>/
        ├── SKILL.md
        ├── agents/openai.yaml
        ├── references/
        └── scripts/
Cada SKILL.md contiene el procedimiento operativo de su especialidad. agents/openai.yaml proporciona los metadatos de interfaz y el prompt inicial. Las carpetas scripts/ y references/ solo contienen recursos reutilizables necesarios para esa skill.

Versionado
Los paquetes ZIP son incrementales y nunca deben sobrescribirse. Los cambios posteriores a una versión empaquetada deben publicarse con el siguiente número disponible.

Antes de distribuir un nuevo ZIP:

Ejecutar validate_pack.py.
Comprobar los scripts incluidos.
Verificar que existan 16 SKILL.md y 16 agents/openai.yaml.
Excluir cachés, dependencias, secretos y archivos temporales.
Calcular y comunicar el SHA-256.
