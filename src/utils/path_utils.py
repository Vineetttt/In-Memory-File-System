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

def parse_echo_command(command_str):
    """Parse the echo command to extract content and file path."""
    redirect_split = command_str.split('>', 1)
    if len(redirect_split) != 2:
        return None, None

    content = redirect_split[0].strip()
    file_path = redirect_split[1].strip()

    if (content.startswith('"') and content.endswith('"')) or (content.startswith("'") and content.endswith("'")):
        content = content[1:-1]  

    return content, file_path