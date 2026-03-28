AGENTS_TEMPLATE = """# AGENTS.md - Guía para el Desarrollo

Este documento establece las directrices y convenciones para los agentes de IA.

## Principios Técnicos
- **SOLID**: Seguir estrictamente los principios SOLID.
- **TDD**: Escribir pruebas antes de implementar el código.
- **Tipado Estricto**: Usar type hints en todo el código Python.
- **Arquitectura Hexagonal**: Mantener la lógica central independiente de los adaptadores externos.

## Estilo de Código
- Usar PEP 8 como guía de estilo.
- Utilizar Black para el formateo automático.
- Mypy para la verificación de tipos.
"""

PROJECT_CONTEXT_TEMPLATE = """# PROJECT_CONTEXT.md

## Descripción del Proyecto
Este archivo contiene el contexto general del proyecto, dependencias clave y cualquier otra información relevante.

## Dependencias
- Python 3.11+
- Pytest
- Pydantic
"""
