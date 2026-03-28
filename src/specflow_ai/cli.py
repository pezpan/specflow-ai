import sys
import argparse
from specflow_ai.core.init_use_case import InitUseCase
from specflow_ai.core.file_system_adapter import FileSystemAdapter

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(description="SpecFlow-AI CLI tool for SDD.")
    subparsers = parser.add_subparsers(dest="command")

    # init command
    init_parser = subparsers.add_parser("init", help="Initialize a new project.")
    
    parsed_args = parser.parse_args(args)

    if parsed_args.command == "init":
        fs_adapter = FileSystemAdapter()
        use_case = InitUseCase(fs_adapter=fs_adapter)
        use_case.execute()
        print("Project initialized successfully.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
