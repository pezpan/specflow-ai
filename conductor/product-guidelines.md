# Product Guidelines: SpecFlow-AI

## 1. Communication & Tone
*   **Empathetic & Guiding:** SpecFlow-AI should use approachable language that guides the user through the SDD process. It should provide helpful tips and clear examples to reduce the learning curve.
*   **Inclusive Language:** All user-facing text must be accessible and inclusive, avoiding jargon where possible or explaining it clearly when necessary.

## 2. Error Handling & Reporting
*   **Comprehensive Diagnostics:** When an error occurs, the system should provide a detailed report including stack traces (where appropriate) and references to relevant log files.
*   **Actionable Fixes:** For common errors (e.g., malformed Gherkin, missing dependencies), the CLI should suggest specific commands or manual fixes to resolve the issue.
*   **Structured Feedback:** Error summaries and complex validation results should be presented in a structured format, such as tables or bulleted lists, to improve readability.

## 3. Transparency & Progress
*   **Milestone-Based Progress:** During long-running operations like `/sdd.implement`, the system should provide updates as high-level milestones are reached (e.g., "Tests for [Feature X] passed").
*   **Clear State Indication:** The user should always know what the current state of the project is and what the next logical step should be.

## 4. User Interface Principles
*   **Classic CLI Patterns:** Follow established CLI design conventions (e.g., Git-like command structures: `sdd init`, `sdd specify`) to ensure a familiar experience for developers.
*   **Accessibility First:** Prioritize screen-reader compatibility and high-contrast output. Avoid over-reliance on color alone to convey meaning.
*   **Terminal Stability:** Ensure that the output remains clean and does not clutter the terminal window unnecessarily.
