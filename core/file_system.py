from .file_node import FileNode
from ..utils.path_utils import normalize_path

class FileSystem:
    def __init__(self):
        self.root = FileNode("/", is_directory=True)
        self.current_directory = self.root

    def _get_node_by_path(self, path):
        if not path or path == "/":
            return self.root

        current = self.root if path.startswith("/") else self.current_directory
        parts = normalize_path(path).split("/")
        
        for part in parts:
            if not part or part == ".":
                continue
            if part == "..":
                current = current.parent or current
                continue
            if part not in current.children:
                return None
            current = current.children[part]
        
        return current