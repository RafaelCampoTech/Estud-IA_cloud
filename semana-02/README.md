# Semana 2 · Contenedores e integración continua

Esta semana tu proyecto pasa de ser una idea a algo que otra persona puede ejecutar, y que una máquina puede comprobar cada vez que cambia.

## Mapa de la semana

| Encuentro | Título | Qué te llevas |
|---|---|---|
| 3 | Contenedor, configuración y entorno reproducible | Una imagen y una ejecución identificables que otra persona puede repetir |
| 4 | Integración continua y validación de cambios | Una validación automática con un caso correcto y otro fallido |

## Antes de la semana: lo asincrónico en Platzi

**M3 · Despliegue de aplicaciones en la nube**
- Elastic Beanstalk (AWS) y App Engine (GCP): desplegar sin gestionar servidores
- Variables de entorno y gestión de secretos
- Estrategias de despliegue: rolling, blue-green y canary
- Health checks y reintentos automáticos
- Rollback: recuperar la versión anterior ante un fallo

Además retomamos lo de la semana 1: ciclo de vida de imágenes, redes, volúmenes y Compose (M2), y CI/CD con GitHub Actions (M1).

## Qué vas a aprender

**Encuentro 3 · Contenedor y entorno reproducible**
- Distinguir **imagen**, **contenedor**, **configuración** y **persistencia**.
- Construir, identificar y ejecutar una imagen, y explicar qué queda dentro de ella y qué se aporta al iniciar.
- Diferenciar una etiqueta de la identificación de una versión concreta.
- Recorrer el puerto de la aplicación y su publicación local.
- Ver la diferencia entre un dato efímero y uno persistido.
- Dejar instrucciones para que **otra persona** arranque tu servicio sin ayuda.

**Encuentro 4 · Integración continua**
- Recorrer disparador (trigger), job y pasos mientras se ejecuta una prueba.
- Leer el mensaje de un fallo y entender qué lo causó.
- Entender por qué un resultado exitoso solo acredita las comprobaciones que realmente se ejecutaron.
- Distinguir integración continua de despliegue controlado: que el job corra no significa que haya un bloqueo de promoción.
- Separar secretos del sistema de CI, variables no sensibles y credenciales de tu equipo.
- Comparar, según tu necesidad, GitHub Actions, los pipelines nativos del proveedor y GitOps. No necesitas construir varios.

## Evidencias flexibles

- Imagen y ejecución identificables, o una simulación declarada.
- Configuración y persistencia explicadas.
- Un arranque seguido por otra persona, con evidencia.
- Una validación con caso correcto y caso fallido, y el log interpretado.
- La condición de avance explicitada, y los permisos y el alcance reales del pipeline.

## Para llevar a la semana 3

Guarda la versión de tu imagen, tus instrucciones y tu workflow con su estado real de promoción. Identifica **qué parte de tu entorno sigue configurándose a mano**: ahí entra la infraestructura como código.
