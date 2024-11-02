from .base_command import Command
from src.core.file_node import FileNode
from src.utils.path_utils import validate_name, normalize_path

class TouchCommand(Command):
    def execute(self, args):
        if not args:
            print("Error: Missing file name.")
            return
        
        file_path = args[0]
        path_parts = [p for p in normalize_path(file_path).split('/')]
        
        # Handle absolute vs relative path
        current_node = self.fs.root if file_path.startswith('/') else self.fs.current_directory
        
        # Navigate through the path to find the parent directory
        for part in path_parts[:-1]:
            if not part or part == '.':
                continue
            if part == '..':
                if current_node.parent:
                    current_node = current_node.parent
                continue
            if part not in current_node.children or not current_node.children[part].is_directory:
                print(f"Error: Parent directory '{part}' does not exist.")
                return
            current_node = current_node.children[part]
        
        file_name = path_parts[-1]
        
        # Validate the file name
        if not validate_name(file_name):
            print(f"Invalid file name {file_name}.")
            return
            
        # file already exists
        if file_name in current_node.children:
            print(f"Error: File '{file_name}' already exists.")
            return
            
        # Create the new empty file
        new_file = FileNode(name=file_name, is_directory=False, content="")
        new_file.parent = current_node
        current_node.children[file_name] = new_file
        
        print(f"File '{file_path}' created.")