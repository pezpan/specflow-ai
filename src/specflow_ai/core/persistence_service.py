from specflow_ai.core.file_system_adapter import FileSystemAdapter

class PersistenceService:
    """
    Handles file persistence for the spec generation process.
    """
    def __init__(self, fs_adapter: FileSystemAdapter):
        self.fs_adapter = fs_adapter

    def save_spec(self, feature_name: str, content: str) -> str:
        """
        Saves the spec content to the appropriate directory.
        """
        path = f"specs/{feature_name}/spec.md"
        self.fs_adapter.create_file(path, content)
        return path
