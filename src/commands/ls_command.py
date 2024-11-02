from .base_command import Command
from src.utils.path_utils import normalize_path, get_full_path

class LsCommand(Command):
    def execute(self, args):
        # target directory
        target_path = args[0] if args else "."
        
        # target directory node
        if target_path == ".":
            target_node = self.fs.current_directory
        else:
            normalized_path = normalize_path(target_path)
            target_node = self.fs._get_node_by_path(normalized_path)
            
            if target_node is None:
                print(f"Error: '{target_path}' does not exist.")
                return
            
            if not target_node.is_directory:
                print(f"Error: '{target_path}' is not a directory.")
                return

        # Get and sort contents
        contents = list(target_node.children.items())
        
        # Separate directories and files
        directories = [name for name, node in contents if node.is_directory]
        files = [name for name, node in contents if not node.is_directory]

        # directories first
        for dir_name in directories:
            print(dir_name + "/")
            
        # then files
        for file_name in files:
            print(file_name)
            
        # ls directory is empty
        if not contents:
            print("(empty directory)")