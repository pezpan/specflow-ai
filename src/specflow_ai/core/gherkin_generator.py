from typing import Any

class GherkinGenerator:
    """
    Generates Gherkin-formatted strings from gathered data.
    """
    def generate(self, data: dict[str, Any]) -> str:
        """
        Creates a Gherkin specification string.
        """
        # Ensure required keys exist
        required_keys = ["feature_name", "scenario_name", "given", "when", "then"]
        for key in required_keys:
            if key not in data:
                raise KeyError(f"Missing required key for Gherkin generation: {key}")

        lines = [
            f"Característica: {data['feature_name']}",
            "",
            f"  Escenario: {data['scenario_name']}",
            f"    Dado {data['given']}",
            f"    Cuando {data['when']}",
            f"    Entonces {data['then']}"
        ]
        
        return "\n".join(lines)
