from src.core.file_system import FileSystem
from src.cli.command_parser import CommandParser

def main():
    fs = FileSystem()
    parser = CommandParser(fs)
    
    print("In-Memory File System initialized. Type 'exit' to quit.")
    
    while True:
        try:
            command = input("$ ").strip()
            if command.lower() == 'exit':
                break
            parser.parse_and_execute(command)
        except KeyboardInterrupt:
            print("\nUse 'exit' to quit.")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()