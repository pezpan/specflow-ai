from specflow_ai.core.init_port import InitPort
from specflow_ai.core.file_system_adapter import FileSystemAdapter
from specflow_ai.core import templates

class InitUseCase(InitPort):
    def __init__(self, fs_adapter: FileSystemAdapter):
        self.fs_adapter = fs_adapter

    def execute(self) -> None:
        """
        Executes the initialization process by creating the required directory structure and files.
        """
        # Create directories
        self.fs_adapter.create_directory("prompts")
        self.fs_adapter.create_directory("skills")

        # Create files
        self.fs_adapter.create_file("AGENTS.md", templates.AGENTS_TEMPLATE)
        self.fs_adapter.create_file("PROJECT_CONTEXT.md", templates.PROJECT_CONTEXT_TEMPLATE)
