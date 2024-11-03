from .base_command import Command
from src.utils.path_utils import (
    normalize_path, 
    validate_name, 
    get_destination_node,
    move_node
)

class MvCommand(Command):
    def execute(self, args):
        if len(args) != 2:
            print("Error: mv command requires source and destination paths.")
            return

        source_path = args[0]
        dest_path = args[1]

        # source node and its parent
        source_node = self.fs._get_node_by_path(source_path)
        if not source_node:
            print(f"Error: Source '{source_path}' does not exist.")
            return

        source_parent = source_node.parent
        if not source_parent:
            print("Error: Cannot move root directory.")
            return

        # destination information
        dest_parent, final_name, _ = get_destination_node(self.fs, dest_path)
        if not dest_parent:
            return
        
        if not final_name:
            final_name = source_node.name
            
        if move_node(source_node, source_parent, dest_parent, final_name):
            print(f"Moved '{source_path}' to '{dest_path}'")