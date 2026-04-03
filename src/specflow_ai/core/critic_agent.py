from dataclasses import dataclass, field
import re

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
        
        # Syntax Checks
        has_feature = "Característica:" in content or "Feature:" in content
        has_scenario = "Escenario:" in content or "Scenario:" in content
        has_given = "Dado" in content or "Given" in content
        has_when = "Cuando" in content or "When" in content
        has_then = "Entonces" in content or "Then" in content
        
        if not all([has_feature, has_scenario, has_given, has_when, has_then]):
            issues.append("Missing Gherkin keywords (Característica, Escenario, Dado, Cuando, Entonces)")
            
        # Consistency Checks
        if all([has_given, has_then]):
            # Extract content after keywords
            given_match = re.search(r"(?:Dado|Given)\s+(.*)", content)
            then_match = re.search(r"(?:Entonces|Then)\s+(.*)", content)
            
            if given_match and then_match:
                given_text = given_match.group(1).strip()
                then_text = then_match.group(1).strip()
                
                if given_text == then_text:
                    issues.append("Redundancy detected: Given and Then conditions are identical")
            
        return ValidationResult(is_valid=len(issues) == 0, issues=issues)
