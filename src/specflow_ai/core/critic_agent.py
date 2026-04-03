from dataclasses import dataclass, field

@dataclass
class ValidationResult:
    """
    Represents the result of a semantic validation.
    """
    is_valid: bool
    issues: list[str] = field(default_factory=list)

class CriticAgent:
    """
    Reviews and validates specifications for coherence and syntax.
    """
    def validate(self, content: str) -> ValidationResult:
        """
        Performs validation on the provided Gherkin content.
        """
        issues = []
        
        # Simple rule-based validation for now
        keywords = ["Característica:", "Escenario:", "Dado", "Cuando", "Entonces"]
        missing = [kw for key in [["Característica:", "Feature:"], ["Escenario:", "Scenario:"]] if not any(k in content for k in key) for kw in [key[0]]]
        # Wait, the rule above is confusing. Let's simplify.
        
        has_feature = "Característica:" in content or "Feature:" in content
        has_scenario = "Escenario:" in content or "Scenario:" in content
        has_given = "Dado" in content or "Given" in content
        has_when = "Cuando" in content or "When" in content
        has_then = "Entonces" in content or "Then" in content
        
        if not all([has_feature, has_scenario, has_given, has_when, has_then]):
            issues.append("Missing Gherkin keywords (Característica, Escenario, Dado, Cuando, Entonces)")
            
        return ValidationResult(is_valid=len(issues) == 0, issues=issues)
