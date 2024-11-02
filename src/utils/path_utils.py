import re

def normalize_path(path):
    """Normalize a file system path."""
    if not path:
        return "."
    while "//" in path:
        path = path.replace("//", "/")
    if path != "/" and path.endswith("/"):
        path = path[:-1]
    return path

def validate_name(name):
        """Validate name against standard rules."""
        if not name or name.isspace():
            print("Error: Directory name cannot be empty or whitespace.")
            return False
        if len(name) > 255:
            print("Error: Directory name cannot exceed 255 characters.")
            return False
        if re.search(r'[<>:"/\\|?*]', name):
            print("Error: Directory name contains invalid characters.")
            return False
        return True

def get_full_path(node):
    """Get the full path of a node."""
    if not node:
        return "/"
        
    path_parts = []
    current = node
    while current and current.name != "/":
        path_parts.append(current.name)
        current = current.parent
        
    if not path_parts:
        return "/"
    return "/" + "/".join(reversed(path_parts))