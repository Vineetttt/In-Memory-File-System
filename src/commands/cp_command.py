from .base_command import Command
from src.core.file_node import FileNode
from src.utils.path_utils import normalize_path, validate_name, get_destination_node, copy_node
from datetime import datetime

class CpCommand(Command):
    def execute(self, args):
        if len(args) != 2:
            print("Error: cp command requires source and destination paths.")
            return

        source_path = args[0]
        dest_path = args[1]

        # source node
        source_node = self.fs._get_node_by_path(source_path)
        if not source_node:
            print(f"Error: Source '{source_path}' does not exist.")
            return

        # destination
        dest_parent, final_name, _ = get_destination_node(self.fs, dest_path)
        if not dest_parent:
            return

        if not final_name:
            final_name = source_node.name
            
        if copy_node(source_node, dest_parent, final_name):
            node_type = "directory" if source_node.is_directory else "file"
            print(f"Copied {node_type} '{source_path}' to '{dest_path}'")