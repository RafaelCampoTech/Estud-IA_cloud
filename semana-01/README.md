# Semana 1 · Necesidad, alcance y pruebas de aceptación

Esta semana no empieza por una herramienta, sino por un problema: ¿qué dificultad de operación vale la pena automatizar? Al terminar, tendrás una necesidad explicada, una ficha de tu servicio y dos criterios para saber si funciona.

## Mapa de la semana

| Encuentro | Título | Qué te llevas |
|---|---|---|
| 1 | Comunidad, pacto y desafíos de operación | Una oportunidad con usuario y dificultad operativa, y una pregunta sobre cómo comprobarla |
| 2 | Alcance, arquitectura y pruebas de aceptación | Un brief con alcance incluido y excluido, un diagrama inicial y dos pruebas de aceptación |

## Antes de la semana: lo asincrónico en Platzi

Esta semana se apoya en dos módulos que ves en Platzi:

**M1 · CI/CD y DevOps en la nube**
- Pipelines con GitHub Actions: jobs, steps, triggers y artefactos
- Pipelines nativos del proveedor: CodePipeline + CodeBuild (AWS) o Cloud Build (GCP)
- Análisis de código estático (linting, SAST) dentro del pipeline
- Gestión de entornos: dev, staging y prod, con variables y aprobaciones manuales
- Estrategia GitOps: sincronizar el estado deseado del clúster desde el repositorio

**M2 · Contenedores con Docker y Kubernetes**
- Ciclo de vida de una imagen: Dockerfile, build, tag, push y pull
- Redes y volúmenes en Docker: bridge, host y bind mounts
- Docker Compose para aplicaciones de varios contenedores
- Fundamentos de Kubernetes y `kubectl` básico
- Distribución de contenedores en registros

Si no alcanzaste a verlos, no pasa nada. En los encuentros los usamos para pensar tu proyecto, no para examinarte.

## Qué vas a aprender

**Encuentro 1**
- Reconocer problemas de operación: un entorno que se reconstruye a mano, una versión que sale con fallas.
- Distinguir una instrucción manual ambigua de una ejecución pequeña que conserva versión y resultado.
- Redactar una oportunidad: quién es el usuario y qué le cuesta.
- Preguntarte qué evidencia necesitarías para afirmar que algo puede repetirse.

**Encuentro 2**
- Completar la **ficha** de tu servicio: usuario, servicio, componentes, entornos, dependencias y recursos.
- Decidir qué entra y qué queda fuera de tu alcance.
- Separar **función** de **operación**: que el servicio responda no es lo mismo que poder recuperar una versión anterior.
- Entender qué diferencia a desarrollo de pruebas: configuración, acceso y datos, no solo el nombre.
- Escribir dos criterios de aceptación: una ejecución reproducible y una versión defectuosa que no se promueve o puede revertirse.
- Ver dónde caben, en tu recorrido, un trigger, un job, una validación y una aprobación manual. Sin construir todavía un pipeline.

## Vocabulario de la semana

| Término | Qué significa aquí |
|---|---|
| Oportunidad | Una dificultad de operación de un usuario real que vale la pena resolver |
| Ficha | Una página que describe tu servicio: usuario, componentes, entornos, dependencias y recursos |
| Criterio de aceptación | Una condición observable que te dice si el recorrido funciona |
| Entorno | Un lugar donde corre el servicio, con su propia configuración, acceso y datos |
| Evidencia | Un log, una salida o una captura que respalda lo que afirmas |

## Evidencias flexibles

- Una oportunidad con usuario y dificultad operativa.
- Una duda sobre el entorno o los recursos.
- Un brief con alcance incluido y excluido.
- Un diagrama inicial y dos pruebas de aceptación.

Sirven para conversar. No son entregas administrativas.

## Para llevar a la semana 2

Guarda tu brief, tu diagrama y tus criterios. Identifica qué necesitas para construir tu **primera ejecución reproducible**. En la semana 2 la imagen y la configuración serán el medio para sostener el recorrido que acordaste.
