from .base_command import Command
from src.utils.path_utils import normalize_path

class RmCommand(Command):
    def execute(self, args):
        if not args:
            print("Error: Missing path argument.")
            return
            
        # -r ?
        recursive = False
        path = args[0]
        
        if len(args) > 1 and args[0] == "-r":
            recursive = True
            path = args[1]
        
        # target node and its parent
        target_node = self.fs._get_node_by_path(path)
        if not target_node:
            print(f"Error: '{path}' does not exist.")
            return
            
        # remove root directory not possible
        if target_node == self.fs.root:
            print("Error: Cannot remove root directory.")
            return
            
        # directory ?
        if target_node.is_directory:
            if not recursive and target_node.children:
                print(f"Error: '{path}' is a non-empty directory. Use -r flag to remove recursively.")
                return
                
            current = self.fs.current_directory
            while current:
                if current == target_node:
                    self.fs.current_directory = target_node.parent
                    break
                current = current.parent
        
        # remove node from its parent's children
        parent = target_node.parent
        del parent.children[target_node.name]
        
        node_type = "directory" if target_node.is_directory else "file"
        print(f"Removed {node_type} '{path}'")