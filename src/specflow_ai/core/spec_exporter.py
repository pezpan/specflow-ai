from datetime import datetime
from typing import Any

class SpecExporter:
    """
    Exports various sections of the spec.md file.
    """
    def export_metadata(self, data: dict[str, Any]) -> str:
        """
        Generates the Metadata section.
        """
        author = data.get("author", "Unknown")
        version = data.get("version", "0.1.0")
        date = datetime.now().strftime("%Y-%m-%d")
        
        lines = [
            "## Metadata",
            f"- **Author**: {author}",
            f"- **Version**: {version}",
            f"- **Date**: {date}"
        ]
        return "\n".join(lines)

    def export_out_of_scope(self, data: dict[str, Any]) -> str:
        """
        Generates the Out of Scope section.
        """
        items = data.get("out_of_scope", [])
        lines = ["## Out of Scope"]
        if not items:
            lines.append("None identified.")
        else:
            for item in items:
                lines.append(f"- {item}")
        return "\n".join(lines)

    def export_history(self, data: dict[str, Any]) -> str:
        """
        Generates the Dialogue History section.
        """
        questions = data.get("questions", [])
        answers = data.get("answers", [])
        
        lines = ["## Dialogue History"]
        for q, a in zip(questions, answers):
            lines.append(f"### Q: {q}")
            lines.append(f"A: {a}")
            lines.append("")
        return "\n".join(lines).strip()
