# Specification: Implement the core /sdd.specify command flow for Master Plan Mode

## 1. Overview
The `/sdd.specify` command activates the "Master Plan Mode" in SpecFlow-AI. Its primary goal is to guide the user through a structured, interactive dialogue to refine software requirements and generate a high-quality, semantically validated specification in Gherkin format.

## 2. Functional Requirements
### 2.1 Master Plan Mode (Interrogation)
*   **Trigger:** Activated when the user executes `/sdd.specify`.
*   **Iterative Dialogue:** The agent must engage in a multi-turn conversation, asking one critical question at a time to resolve ambiguities.
*   **Question Threshold:** The agent **must** ask at least 3 critical questions before it is allowed to generate the final specification.
*   **Vagueness Guard:** If the user's input is too vague, the agent must pause and request specific clarification before proceeding.

### 2.2 Specification Generation
*   **Gherkin Output:** The final output must strictly follow the "Given/When/Then" (Dado/Cuando/Entonces) format.
*   **File Structure:**
    *   **Metadata Header:** Include creation date, author, and version.
    *   **Out of Scope Section:** Explicitly list any items identified as out of scope during the dialogue.
    *   **Dialogue History:** Include the 3+ critical questions and the user's corresponding answers.
*   **Persistence:** The resulting specification must be saved to `specs/{feature_name}/spec.md`.

### 2.3 Semantic Validation (The "Critic" Agent)
*   **Strict Blocking:** After the specification is drafted, a specialized "Critic" agent must review it for coherence, syntax (Syntax Enforcement), and logical contradictions (Consistency Check).
*   **Validation Protocol:** If the Critic identifies issues, it must block the final validation and provide a structured list of corrections. The user must address these issues before the specification is considered valid.

## 3. Acceptance Criteria
*   [ ] The command `/sdd.specify` initiates a multi-turn dialogue.
*   [ ] The agent asks at least 3 critical questions based on the user's initial input.
*   [ ] A `spec.md` file is generated with Metadata, Out of Scope, and Dialogue History sections.
*   [ ] All generated scenarios follow the Gherkin syntax.
*   [ ] The "Critic" agent identifies logical contradictions and blocks invalid specifications.
*   [ ] Errors are gracefully handled for empty or highly contradictory user input.
