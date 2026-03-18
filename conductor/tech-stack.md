# Technology Stack: SpecFlow-AI

## 1. Programming Language
*   **Python 3.11+:** The core development language, chosen for its extensive ecosystem of AI libraries and developer-friendly syntax.
*   **Type Annotations:** Strict `type hints` are required throughout the codebase to ensure type safety and improve maintainability.

## 2. Core Frameworks & Libraries
*   **Testing & TDD:** `pytest` is the primary testing framework, supporting our TDD-driven development approach.
*   **Data Validation:** `Pydantic` is used for robust schema validation, data parsing, and configuration management.
*   **Type Checking:** `mypy` is integrated into the workflow to perform static type verification.
*   **Code Quality:** `Black` (formatting) and `Flake8` (linting) are used to enforce PEP 8 compliance.

## 3. Architecture & Patterns
*   **Hexagonal / Clean Architecture:** Ensures high decoupling between core business logic and external adapters (CLI, AI Models, File System).
*   **SOLID Principles:** All design decisions are guided by SOLID principles to ensure a maintainable and scalable codebase.

## 4. AI & Agent Integration
*   **Autonomous Chain of Thought:** Agents are designed to handle complex task breakdowns and error recovery autonomously.
*   **LLM-as-a-Judge:** Integrated as a mechanism to evaluate subjective code quality and maintainability (reinforced by the 'Critic' agent).
*   **Extensible Model Support:** The architecture allows for switching or combining different LLM providers through standardized ports.
