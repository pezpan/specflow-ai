from pathlib import Path

class FileSystemAdapter:
    def create_directory(self, path: str | Path) -> None:
        """
        Creates a directory at the specified path.
        """
        Path(path).mkdir(parents=True, exist_ok=True)

    def create_file(self, path: str | Path, content: str) -> None:
        """
        Creates a file at the specified path with the provided content.
        """
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content)
