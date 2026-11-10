# Semana 4 · Conectividad, acceso y telemetría

Esta semana miras tu servicio desde afuera y desde adentro: quién puede llegar a él, qué expone de más y cómo sabrás qué pasó cuando algo falla.

## Mapa de la semana

| Encuentro | Título | Qué te llevas |
|---|---|---|
| 7 | Conectividad, acceso y exposición del servicio | Una topología con flujos y fronteras, y dos riesgos con una medida cada uno |
| 8 | Telemetría, alertas y respuesta a incidentes | Una señal útil, una falla controlada y un runbook que otra persona pudo seguir |

## Antes de la semana: lo asincrónico en Platzi

**M5 · Infraestructura como código avanzado con Terraform**
- Módulos reutilizables: estructura, inputs, outputs y registry
- Remote state con S3 + DynamoDB o GCS: bloqueo de estado en equipos
- Workspaces: varios entornos con un solo código
- Terragrunt: evitar repetición en configuraciones multi-entorno
- Detección de drift y reconciliación

Esta semana retomamos redes (M4) y aplicamos IaC (M5) con revisión de drift. El Encuentro 8 anticipa el módulo M6 de observabilidad, que verás en Platzi la semana siguiente.

## Qué vas a aprender

**Encuentro 7 · Conectividad y exposición**
- Recorrer el camino de una petición y señalar una exposición que el usuario no necesita.
- Distinguir un fallo de DNS de uno de permiso por sus síntomas.
- Elegir entre balanceo de aplicación y de red según el tipo de tráfico, no por el nombre del producto.
- Entender qué problema atienden WAF y la conectividad privada, y qué **no** reemplazan: un control de tráfico no sustituye identidad ni autorización de la aplicación.
- Comparar red interna y puertos publicados.
- Probar una comunicación permitida y una denegada.
- Diferenciar un control **diseñado** de uno **aplicado**.

**Encuentro 8 · Telemetría y respuesta**
- Seguir una petición en los registros y relacionar tiempos y respuesta.
- Distinguir qué aporta una métrica agregada y qué detalle da un log o una traza.
- Conocer OpenTelemetry y dónde termina la instrumentación real.
- Diseñar una alerta accionable que no genere ruido continuo.
- Escribir y probar un runbook con una comprobación inicial.
- Registrar síntoma, evidencia, hipótesis y decisión, sin inventar una causa porque dos señales cambiaron al mismo tiempo.

## Evidencias flexibles

- Una topología con flujos y fronteras de acceso.
- Dos riesgos revisados y controles con su alcance real.
- Una comprobación permitida y una restricción documentadas.
- Una señal relacionada con tu servicio y su procedencia.
- Una falla controlada y un runbook seguido por un tercero.
- Los límites de lo que observas.

## Ojo con estas ideas

- Abrir un puerto para que "conecte" no es una solución final.
- Un WAF no protege de todo ataque.
- La ausencia de una señal no demuestra que el componente esté sano.
- No subas el umbral de una alerta solo para ocultar una falla.

## Para llevar a la semana 5

Guarda tu topología, tus riesgos, tu telemetría y tu runbook revisado. Identifica **una evidencia que otra persona deba poder seguir** durante la auditoría. Antes de la semana 5, completa el módulo M6 en Platzi.
