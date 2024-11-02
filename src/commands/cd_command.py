from .base_command import Command
from src.core.file_node import FileNode
from src.utils.path_utils import normalize_path, get_full_path

class CdCommand(Command):
    def execute(self, args):
        if not args:
            # change to root directory
            self.fs.current_directory = self.fs.root
            print(f"Changed to root: /")
            return

        path = args[0]
        normalized_path = normalize_path(path)
        
        if normalized_path == "/":
            self.fs.current_directory = self.fs.root
            print("Changed to root: /")
            return
        elif normalized_path == ".":
            current_path = get_full_path(self.fs.current_directory)
            print(f"Current directory: {current_path}")
            return
        elif normalized_path == "..":
            if self.fs.current_directory.parent:
                self.fs.current_directory = self.fs.current_directory.parent
                new_path = get_full_path(self.fs.current_directory)
                print(f"Changed to parent: {new_path}")
            return

        target_node = self.fs._get_node_by_path(normalized_path)
        
        if target_node is None:
            print(f"Error: Directory '{path}' does not exist.")
            return
            
        if not target_node.is_directory:
            print(f"Error: '{path}' is not a directory.")
            return
            
        self.fs.current_directory = target_node
        new_path = get_full_path(self.fs.current_directory)
        print(f"Changed to: {new_path}")