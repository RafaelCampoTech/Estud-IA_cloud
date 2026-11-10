# Semana 3 · Infraestructura declarativa, actualización y reversión

Esta semana aprendes a describir tu servicio como código, a actualizarlo con confianza y a volver atrás cuando algo sale mal.

## Mapa de la semana

| Encuentro | Título | Qué te llevas |
|---|---|---|
| 5 | Infraestructura declarativa y manejo de entornos | Un componente descrito como código, con un plan o una validación interpretados |
| 6 | Actualización, salud y reversión | Una versión estable y otra defectuosa, y la reversión ensayada |

## Antes de la semana: lo asincrónico en Platzi

**M4 · Redes avanzadas y conectividad**
- VPC peering y Transit Gateway (AWS), Cloud Router (GCP)
- DNS con Route 53 y Cloud DNS: routing por latencia y failover
- WAF: reglas gestionadas y personalizadas contra OWASP Top 10
- Private Link y Private Service Connect
- Network Load Balancer frente a Application Load Balancer

También retomamos el despliegue de la semana 2 (M3) y Kubernetes básico (M2) si tu proyecto lo usa. El Encuentro 5 anticipa el módulo M5 de Terraform, que verás en Platzi la semana siguiente.

## Qué vas a aprender

**Encuentro 5 · Infraestructura declarativa**
- Leer un módulo: entradas, salidas y estructura.
- Usar formato y validación, y saber **qué no comprueban** sobre el entorno real.
- Leer un plan y distinguir crear, modificar y reemplazar.
- Entender qué es el **estado**, cómo relaciona la configuración con los recursos y por qué necesita control de acceso.
- Comparar mecanismos de separación de entornos (workspaces, carpetas) y por qué no equivalen, por sí solos, a aislamiento de permisos.
- Reconocer una divergencia entre lo descrito y lo que existe.

**Encuentro 6 · Actualización, salud y reversión**
- Publicar una versión con una falla controlada y leer la comprobación de salud.
- Decidir qué condición detiene el avance de una actualización.
- Recuperar la versión anterior y repetir la operación de usuario para verificarla.
- Comparar rolling, blue-green y canary según las condiciones del servicio.
- Si usas Kubernetes: distinguir *readiness* de *liveness* y entender qué pregunta responde cada sonda.
- Identificar la versión activa con una referencia estable, no con una etiqueta que cambia.

## Evidencias flexibles

- Un componente de infraestructura como código con entradas y salidas comprensibles.
- Una validación o un plan interpretados, con el alcance declarado.
- Cómo controlas el estado y qué diferencia a tus entornos.
- Versiones identificables y una prueba de salud.
- Un cambio y una reversión ejecutados, o una simulación declarada.
- Las dependencias que limitan la recuperación (por ejemplo, datos incompatibles con la versión anterior).

## Ojo con estas ideas

- Una validación correcta no significa que la infraestructura exista.
- Revertir un contenedor no garantiza revertir toda la solución.
- Una sonda mal diseñada puede ocultar una dependencia o provocar reinicios.

## Para llevar a la semana 4

Guarda tu configuración, tu registro de validación o plan, y tus versiones con la evidencia del ensayo. Señala **una dependencia de red o de acceso** que podría impedirte distinguir un fallo de versión de un fallo de conexión.
