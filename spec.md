# Documento de Especificación: SpecFlow-AI

## 1. Introducción

SpecFlow-AI es una herramienta diseñada para revolucionar el desarrollo de software a través del Spec-Driven Development (SDD) mediante la integración de capacidades de Inteligencia Artificial. La idea central es construir una serie de comandos (slash commands) en Python que faciliten y automaticen el desarrollo, permitiendo que las especificaciones sean "ejecutables" por agentes de IA. Esto busca minimizar la intervención manual en el código, mejorar la calidad del software y acelerar el ciclo de desarrollo.

## 2. Visión del Producto

SpecFlow-AI busca ser el asistente definitivo para equipos de desarrollo que adoptan metodologías BDD/SDD, proporcionando un flujo de trabajo intuitivo y automatizado desde la concepción de una idea hasta la implementación y validación. La herramienta permitirá a los usuarios definir sus requisitos de negocio en un lenguaje natural (Gherkin), y delegar la traducción de esas especificaciones a código ejecutable y pruebas a agentes de IA, garantizando que el software entregado cumpla estrictamente con las expectativas.

## 3. Público Objetivo

*   **Desarrolladores de Software:** Buscan herramientas que automaticen tareas repetitivas y mejoren la calidad del código.
*   **QA Engineers / Testers:** Necesitan asegurar que las pruebas de aceptación estén siempre alineadas con las especificaciones y que se ejecuten de manera eficiente.
*   **Product Owners / Business Analysts:** Quieren una forma clara y ejecutable de definir los requisitos del negocio, reduciendo la ambigüedad y mejorando la comunicación con el equipo técnico.

## 4. Comandos Principales y Flujo de Trabajo

El usuario interactuará con SpecFlow-AI a través de una serie de slash commands que guiarán el proceso de desarrollo:

### 4.1. `/sdd.init`

**Descripción:** Inicializa un nuevo proyecto SpecFlow-AI en el directorio actual. Establece la estructura básica del proyecto y los principios de gobierno.

**Flujo Esperado:**
1.  El usuario ejecuta `/sdd.init`.
2.  La herramienta crea la siguiente estructura de archivos y directorios:
    *   `AGENTS.md`: Documento con las reglas técnicas y convenciones para los agentes de IA (SOLID, TDD, tipado estricto, PEP 8, etc.).
    *   `PROJECT_CONTEXT.md`: Archivo para describir el contexto general del proyecto, dependencias clave, y cualquier otra información relevante.
    *   `prompts/`: Directorio para almacenar los prompts y directrices específicas para los agentes.
    *   `skills/`: Directorio para definir las habilidades que los agentes pueden utilizar.
3.  El usuario recibe una confirmación de que el proyecto ha sido inicializado exitosamente.

### 4.2. `/sdd.specify`

**Descripción:** Activa el "Modo Master Plan" donde un agente de IA interactúa con el usuario para definir y refinar las Historias de Usuario y los Criterios de Aceptación en formato Gherkin, que se guardan en `spec.md`.

**Flujo Esperado:**
1.  El usuario ejecuta `/sdd.specify`.
2.  Un agente con rol de "Product Manager" (similar a la interacción actual) inicia una conversación con el usuario.
3.  El agente interroga al usuario, formulando preguntas para eliminar ambigüedades y capturar los requisitos de forma detallada.
4.  El agente genera o actualiza el archivo `spec.md` con las Historias de Usuario y sus Criterios de Aceptación en formato Gherkin (Dado/Cuando/Entonces).
5.  Antes de finalizar, un agente "Critic" valida la sintaxis y coherencia de los escenarios Gherkin en `spec.md`.
6.  Si hay errores, el agente "Critic" proporciona una lista estructurada de correcciones necesarias al usuario.
7.  Una vez validado, el usuario confirma la finalización del modo "specify".

### 4.3. `/sdd.plan`

**Descripción:** Lee el `spec.md` y genera un `plan.md` técnico que detalla la arquitectura propuesta, la estructura de archivos y las dependencias clave para implementar las funcionalidades descritas en las especificaciones.

**Flujo Esperado:**
1.  El usuario ejecuta `/sdd.plan`.
2.  La herramienta verifica la existencia y validez de `spec.md`.
3.  Un agente con rol de "Arquitecto de Software" analiza `spec.md`.
4.  El agente genera `plan.md` con la siguiente información (formato Markdown):
    *   **Arquitectura Propuesta:** Diagramas (Mermaid.js) o descripciones de la arquitectura (e.g., Hexagonal, Clean Architecture).
    *   **Estructura de Archivos:** Propuesta de directorios y archivos, siguiendo las convenciones de `AGENTS.md`.
    *   **Dependencias:** Lista de bibliotecas y frameworks Python necesarios (`Pydantic`, `pytest`, etc.) y cómo instalarlos.
    *   **Consideraciones de Diseño:** Decisiones clave sobre patrones, interfaces, etc.
5.  El usuario recibe una notificación de que `plan.md` ha sido generado.

### 4.4. `/sdd.tasks`

**Descripción:** Desglosa el `plan.md` en tareas atómicas y testeables, que se registran en un `tasks.md`. Cada tarea debe ser lo suficientemente pequeña como para ser implementada y probada de forma independiente.

**Flujo Esperado:**
1.  El usuario ejecuta `/sdd.tasks`.
2.  La herramienta verifica la existencia y validez de `plan.md`.
3.  Un agente con rol de "Ingeniero de Software" lee `plan.md` y lo desglosa en una lista de tareas (`tasks.md`).
4.  Cada tarea en `tasks.md` debe incluir:
    *   Una descripción clara.
    *   Los archivos que se espera modificar o crear.
    *   Los criterios de finalización (cómo se valida que la tarea está "hecha").
    *   Un estado inicial (`[ ]` para no completada).
5.  El usuario recibe una notificación de que `tasks.md` ha sido generado.

### 4.5. `/sdd.implement`

**Descripción:** El agente de IA ejecuta las tareas definidas en `tasks.md` una por una. A medida que completa cada tarea (implementación de código, pruebas unitarias y de integración), actualiza el estado en `tasks.md`.

**Flujo Esperado:**
1.  El usuario ejecuta `/sdd.implement`.
2.  La herramienta verifica la existencia y validez de `tasks.md`.
3.  Un agente con rol de "Desarrollador de IA" lee `tasks.md`.
4.  Para cada tarea en `tasks.md`:
    *   El agente actualiza el estado de la tarea a `[x]` (completada) solo cuando la implementación de código y sus pruebas asociadas (unitarias, de integración) pasan (`pytest` en verde).
    *   Si una tarea falla (tests en rojo, errores de compilación, etc.), el agente detiene la ejecución, reporta el error de manera estructurada al usuario, y sugiere posibles soluciones o correcciones.
5.  La percepción del usuario de la progresión se realiza a través de las actualizaciones en `tasks.md`.
6.  Una vez que todas las tareas se han completado, el usuario recibe un informe final.

## 5. Manejo de Casos de Borde y Errores

SpecFlow-AI está diseñado para ser robusto y proporcionar retroalimentación clara en situaciones inesperadas.

### 5.1. Prerrequisitos Faltantes

*   **Detección:** Si un usuario intenta ejecutar un comando sin que los archivos o el estado previo requerido existan (e.g., `/sdd.plan` sin `spec.md`), la herramienta detectará la falta del prerrequisito.
*   **Respuesta:** La herramienta emitirá un error de "Prerrequisito Faltante" y sugerirá el comando correcto que el usuario debe ejecutar para alcanzar la fase actual (e.g., "Error: `spec.md` no encontrado. Por favor, ejecute `/sdd.specify` primero.").

### 5.2. Errores en Especificaciones (Gherkin mal formado)

*   **Agente Critic:** Durante la fase `/sdd.specify`, un agente especializado (Agente Critic) se encargará de validar la sintaxis Gherkin y la coherencia lógica de las Historias de Usuario.
*   **Retroalimentación:** Si se detectan errores, el Agente Critic proporcionará una lista estructurada de correcciones necesarias. Esta lista se presentará en un formato fácil de consumir por el usuario (e.g., JSON o tabla Markdown), indicando la línea, el tipo de error y la sugerencia de corrección.

### 5.3. Problemas de Comunicación y Errores de API

*   **Detección:** El sistema monitoreará activamente los errores de API (códigos 4xx, 5xx), tiempos de espera agotados, y cualquier otra anomalía en la comunicación con los servicios de IA o externos.
*   **Registro:** Cualquier error detectado se registrará con detalles completos (timestamp, endpoint, código de error, mensaje de error) en un archivo de log específico (`sdd.log`).
*   **Opciones de Recuperación:** La herramienta ofrecerá al usuario opciones claras:
    *   **Reintento:** Intentar la operación de nuevo.
    *   **Fallback:** Si aplica, cambiar a un modelo de IA alternativo o a una estrategia de procesamiento menos intensiva.
    *   **Reporte:** Guía para reportar el problema si persiste.
*   **Retroalimentación al Usuario:** La respuesta al usuario incluirá un mensaje claro sobre el problema, la referencia al log de errores y las opciones de recuperación presentadas de forma estructurada.

## 6. Criterios de Éxito

El éxito de SpecFlow-AI se medirá por su impacto directo en la eficiencia y calidad del proceso de desarrollo.

### 6.1. Métricas de Velocidad

*   **Tiempo de Idea a Tarea Ejecutable:** Reducir en un X% (a definir, e.g., 30%) el tiempo promedio que se tarda en pasar de una idea de funcionalidad a tener una lista de tareas en `tasks.md` listas para la implementación agéntica.

### 6.2. Métricas de Calidad

*   **Densidad de Bugs:** Reducir la densidad de bugs (número de bugs por línea de código o por funcionalidad) en un Y% (a definir, e.g., 20%) en proyectos que utilizan SpecFlow-AI, atribuible a la claridad de las especificaciones y la validación continua por parte de los agentes.

### 6.3. Autonomía Agéntica

*   **Porcentaje de Tareas Completadas:** Alcanzar un Z% (a definir, e.g., 85%) de tareas en `tasks.md` que el agente completa con éxito (compilación y tests en verde) sin necesidad de corrección manual significativa por parte del desarrollador.

### 6.4. Alineación con el Contexto y Estándares

*   **Cumplimiento de `AGENTS.md`:** El código generado y modificado por los agentes debe respetar estrictamente las convenciones de `AGENTS.md` (principios SOLID, TDD, tipado estricto, PEP 8) con una tasa de cumplimiento del 95% o superior, verificada por herramientas de linting y tipado (`Black`, `Flake8`, `mypy`) y reportada por el propio agente.

### 6.5. Claridad de Feedback y Contrato de Especificación

*   **Evaluación LLM-as-a-Judge:** Implementar un mecanismo donde un LLM actúe como "Juez" para calificar cualitativamente si el resultado final (código implementado y pruebas) cumple con el "contrato" definido en `spec.md`. Se buscará una calificación promedio de X (e.g., 4/5) o superior en la conformidad con las especificaciones. Esta calificación será una retroalimentación adicional para el desarrollador sobre la "fidelidad" del agente a la intención original.
