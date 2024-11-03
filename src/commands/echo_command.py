from .base_command import Command
from src.core.file_node import FileNode
from src.utils.path_utils import normalize_path, validate_name, parse_echo_command
from datetime import datetime

class EchoCommand(Command):
    def execute(self, args):
        if not args:
            print("Error: No content to echo.")
            return
        content, file_path = parse_echo_command(" ".join(args))
        if not content or not file_path:
            print("Error: Invalid echo command format. Use: echo 'content' > file.txt")
            return

        # directory path and filename
        path_parts = [p for p in normalize_path(file_path).split('/')]
        current_node = self.fs.root if file_path.startswith('/') else self.fs.current_directory

        # navigate to the parent directory
        for part in path_parts[:-1]:
            if not part or part == '.':
                continue
            if part == '..':
                if current_node.parent:
                    current_node = current_node.parent
                continue
            if part not in current_node.children or not current_node.children[part].is_directory:
                print(f"Error: Directory '{part}' does not exist.")
                return
            current_node = current_node.children[part]

        file_name = path_parts[-1]
        if not validate_name(file_name):
            return

        # update if exists
        if file_name in current_node.children:
            file_node = current_node.children[file_name]
            if file_node.is_directory:
                print(f"Error: '{file_name}' is a directory.")
                return
            file_node.content = content
            file_node.modified_at = datetime.now()
            print(f"Content written to existing file '{file_path}'")
        # create new otherwise
        else:
            new_file = FileNode(name=file_name, is_directory=False, content=content)
            new_file.parent = current_node
            current_node.children[file_name] = new_file
            print(f"Content written to new file '{file_path}'")