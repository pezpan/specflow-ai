import sys
import argparse
from specflow_ai.core.init_use_case import InitUseCase
from specflow_ai.core.file_system_adapter import FileSystemAdapter

def main(args: list[str] | None = None) -> None:
    """
    Main entry point for the SpecFlow-AI CLI tool.

    Args:
        args: Optional list of command-line arguments. If None, sys.argv[1:] is used.
    """
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(description="SpecFlow-AI CLI tool for SDD.")
    subparsers = parser.add_subparsers(dest="command")

    # init command
    init_parser = subparsers.add_parser("init", help="Initialize a new project.")
    
    # specify command
    specify_parser = subparsers.add_parser("specify", help="Activate Mode Master Plan to define specs.")
    
    parsed_args = parser.parse_args(args)

    if parsed_args.command == "init":
        fs_adapter = FileSystemAdapter()
        use_case = InitUseCase(fs_adapter=fs_adapter)
        use_case.execute()
        print("Project initialized successfully.")
        print("Created artifacts:")
        print("- Directory: prompts")
        print("- Directory: skills")
        print("- File: AGENTS.md")
        print("- File: PROJECT_CONTEXT.md")
    elif parsed_args.command == "specify":
        print("Entering Mode Master Plan...")
        print("I will guide you to define your User Stories and Acceptance Criteria.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
