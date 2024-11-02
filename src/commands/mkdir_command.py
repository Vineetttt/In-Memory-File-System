from .base_command import Command
from src.core.file_node import FileNode
from src.utils.path_utils import validate_name

class MkdirCommand(Command):
    def execute(self, args):
        if not args:
            print("Error: Missing directory name.")
            return
        
        dir_path = [d for d in args[0].split('/')]
        current_node = self.fs.current_directory

        # Loop through the directory names in the path
        for dir_name in dir_path[:-1]:
            if not validate_name(dir_name):
                return
            # if the parent directory exists
            if dir_name not in current_node.children or not current_node.children[dir_name].is_directory:
                print(f"Error: Parent directory '{dir_name}' does not exist.")
                return
            current_node = current_node.children[dir_name]

        # Check if the final directory already exists
        final_dir_name = dir_path[-1]
        if final_dir_name in current_node.children:
            print(f"Error: Directory '{final_dir_name}' already exists.")
            return
        
        # Create the new directory
        new_dir = FileNode(name=final_dir_name, is_directory=True)
        new_dir.parent = current_node
        current_node.children[final_dir_name] = new_dir
        
        print(f"Directory '{args[0]}' created.")
