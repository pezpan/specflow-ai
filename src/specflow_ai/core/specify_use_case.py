from specflow_ai.core.dialogue_controller import IterativeDialogueController
from specflow_ai.core.gherkin_generator import GherkinGenerator
from specflow_ai.core.spec_exporter import SpecExporter
from specflow_ai.core.persistence_service import PersistenceService
from specflow_ai.core.critic_agent import CriticAgent

class SpecifyUseCase:
    """
    Orchestrates the specification generation process.
    """
    def __init__(
        self,
        dialogue_controller: IterativeDialogueController,
        gherkin_generator: GherkinGenerator,
        spec_exporter: SpecExporter,
        persistence_service: PersistenceService,
        critic_agent: CriticAgent
    ):
        self.dialogue_controller = dialogue_controller
        self.gherkin_generator = gherkin_generator
        self.spec_exporter = spec_exporter
        self.persistence_service = persistence_service
        self.critic_agent = critic_agent

    def execute(self, feature_name: str) -> str:
        """
        Executes the specification generation workflow.
        """
        # 1. Run dialogue
        self.dialogue_controller.run()
        
        # 2. Extract data from state
        state = self.dialogue_controller.state
        data = state.gathered_data
        # Ensure we have feature name in data for generator
        data["feature_name"] = feature_name
        
        # 3. Generate Gherkin
        gherkin = self.gherkin_generator.generate(data)
        
        # 4. Validate with Critic
        validation_result = self.critic_agent.validate(gherkin)
        if not validation_result.is_valid:
            raise ValueError(f"Specification validation failed: {', '.join(validation_result.issues)}")
            
        # 5. Export full spec
        metadata = self.spec_exporter.export_metadata(data)
        out_of_scope = self.spec_exporter.export_out_of_scope(data)
        # We need to pass history data
        # Assuming state has questions/answers lists
        # For now, let's just use empty ones if not present
        history_data = {
            "questions": data.get("history_questions", []),
            "answers": data.get("history_answers", [])
        }
        history = self.spec_exporter.export_history(history_data)
        
        full_content = f"# Specification: {feature_name}\n\n{metadata}\n\n{gherkin}\n\n{out_of_scope}\n\n{history}"
        
        # 6. Save
        return self.persistence_service.save_spec(feature_name, full_content)
