from .base_command import Command
from src.utils.path_utils import normalize_path

class CatCommand(Command):
    def execute(self, args):
        if not args:
            print("Error: Missing file name.")
            return
            
        file_path = args[0]
        normalized_path = normalize_path(file_path)
        target_node = self.fs._get_node_by_path(normalized_path)
        
        if target_node is None:
            print(f"Error: '{file_path}' does not exist.")
            return
            
        if target_node.is_directory:
            print(f"Error: '{file_path}' is a directory.")
            return
        print(target_node.content)