from .base_command import Command
from src.core.file_node import FileNode

class MkdirCommand(Command):
    def execute(self, args):
        if not args:
            print("Error: Missing directory name.")
            return
        
        dir_name = args[0]
        current_node = self.fs.current_directory
        
        # Check if the directory already exists
        if dir_name in current_node.children:
            print(f"Error: Directory '{dir_name}' already exists.")
            return
        
        # Create the new directory
        new_dir = FileNode(name=dir_name, is_directory=True)
        new_dir.parent = current_node
        current_node.children[dir_name] = new_dir
        
        print(f"Directory '{dir_name}' created.")
