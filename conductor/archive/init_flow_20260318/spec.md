# Specification: Implement the core /sdd.init command flow

## 1. Overview
The `/sdd.init` command is the entry point for a new SpecFlow-AI project. Its primary responsibility is to establish the basic project structure and governance principles as defined in the product requirements.

## 2. Requirements
*   Create `AGENTS.md` with technical rules and conventions.
*   Create `PROJECT_CONTEXT.md` for general project context.
*   Create `prompts/` directory for agent guidelines.
*   Create `skills/` directory for agent capabilities.
*   Provide clear terminal feedback upon successful initialization.
*   Adhere to Hexagonal Architecture and SOLID principles.

## 3. Acceptance Criteria
*   The command `sdd init` (or equivalent) executes without error.
*   The specified files and directories are created in the current directory.
*   Existing project files are not overwritten without user confirmation (to be handled in future tracks, but logic should be prepared).
*   Evidence of completion is provided via CLI feedback.
