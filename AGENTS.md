# AGENTES.md - Guía para el Desarrollo de SpecFlow-AI

Este documento establece las directrices y convenciones para los agentes de IA que contribuyan al proyecto SpecFlow-AI, asegurando la coherencia, calidad y cumplimiento de los estándares técnicos.

## Contexto del Proyecto

**Nombre del Proyecto:** SpecFlow-AI

**Descripción:** SpecFlow-AI es un proyecto que busca integrar capacidades de Inteligencia Artificial para mejorar o automatizar aspectos relacionados con el framework SpecFlow, facilitando el desarrollo y mantenimiento de pruebas de aceptación basadas en BDD (Behavior-Driven Development).

**Tecnologías Clave:** Python 3.11+

## Convenciones de Código

Para garantizar la mantenibilidad, escalabilidad y calidad del código, se deben seguir las siguientes convenciones:

*   **Versión de Python:** Se debe utilizar Python 3.11 o superior. Asegúrate de que el entorno de ejecución esté configurado correctamente.
*   **Principios SOLID:** La implementación de cualquier funcionalidad debe adherirse estrictamente a los principios SOLID (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion).
*   **Tipado Estricto:** Es obligatorio el uso de tipado estricto (`type hints`) en todo el código Python. Todas las funciones, métodos y variables deben tener anotaciones de tipo. Se utilizará `mypy` para la verificación estática de tipos.
*   **Arquitectura:** El proyecto debe seguir una arquitectura hexagonal (Ports and Adapters) o una arquitectura limpia (Clean Architecture), promoviendo la separación de preocupaciones y la independencia del framework y la interfaz de usuario.
*   **Testing (TDD):** El desarrollo de nuevas funcionalidades y la corrección de errores deben seguir el enfoque de Desarrollo Guiado por Pruebas (TDD). Esto implica escribir primero las pruebas unitarias y de integración utilizando `pytest` antes de escribir el código de producción. Las pruebas deben cubrir un alto porcentaje del código y ser de alta calidad.
*   **Validación de Datos:** Para la validación de esquemas de datos y la gestión de configuraciones, se utilizará la biblioteca `Pydantic`.
*   **Estilo de Código (PEP 8):** Todo el código debe cumplir con las directrices de estilo de código establecidas en PEP 8. Se recomienda el uso de herramientas de formateo automático como `Black` y `Flake8` para asegurar el cumplimiento.

## Flujo de Trabajo Agéntico

Los agentes de IA que trabajen en este proyecto deben seguir el siguiente flujo de trabajo general:

1.  **Entender el Requerimiento:** Analizar a fondo la tarea o el problema a resolver, identificando las implicaciones en la arquitectura y las convenciones de código.
2.  **Diseño (si aplica):** Si la tarea es una nueva característica, considerar cómo encaja en la arquitectura hexagonal/limpia y cómo se aplicarán los principios SOLID.
3.  **Escribir Pruebas (TDD):** Antes de cualquier cambio en el código de producción, escribir pruebas (unitarias, de integración) con `pytest` que fallen inicialmente y que reflejen el comportamiento esperado de la nueva funcionalidad o la corrección.
4.  **Implementar Código:** Escribir el código de producción necesario para que las pruebas pasen, siguiendo todas las convenciones de código (Python 3.11+, tipado estricto, PEP 8, Pydantic).
5.  **Refactorizar:** Una vez que las pruebas pasen y el código funcione, refactorizarlo para mejorar su diseño, legibilidad y eficiencia, manteniendo siempre los principios SOLID y la arquitectura definida.
6.  **Verificación:** Ejecutar `mypy` para la verificación de tipos, `pytest` para asegurar que todas las pruebas pasen, y `Black`/`Flake8` para el cumplimiento de PEP 8.
7.  **Documentación:** Asegurarse de que cualquier nueva funcionalidad o cambio significativo esté adecuadamente documentado (docstrings, comentarios, actualización de la documentación del proyecto).

Al seguir estas directrices, los agentes de IA contribuirán a un proyecto SpecFlow-AI robusto, mantenible y de alta calidad.