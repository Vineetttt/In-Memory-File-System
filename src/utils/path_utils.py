import re
from src.core.file_node import FileNode
from datetime import datetime 

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

def get_destination_node(fs, path):
    """Get destination node and its parent based on path."""
    path_parts = [p for p in normalize_path(path).split('/') if p and p != '.']
    dest_parent = fs.root if path.startswith('/') else fs.current_directory
    
    for part in path_parts[:-1]:
        if part == '..':
            if dest_parent.parent:
                dest_parent = dest_parent.parent
            continue
        if part not in dest_parent.children or not dest_parent.children[part].is_directory:
            print(f"Error: Directory '{part}' does not exist.")
            return None, None, None
        dest_parent = dest_parent.children[part]
    
    final_name = path_parts[-1] if path_parts else None
    return dest_parent, final_name, path_parts

def move_node(source_node, source_parent, dest_parent, final_name):
    """Move a node from source to destination."""
    if final_name in dest_parent.children:
        if dest_parent.children[final_name].is_directory:
            dest_parent = dest_parent.children[final_name]
            final_name = source_node.name
        else:
            print(f"Error: '{final_name}' already exists in destination.")
            return False

    if not validate_name(final_name):
        return False

    # remove source
    del source_parent.children[source_node.name]
    
    # add destination
    source_node.name = final_name
    source_node.parent = dest_parent
    source_node.modified_at = datetime.now()
    dest_parent.children[final_name] = source_node
    
    return True

def copy_node(source_node, dest_parent, final_name):
        """Copy a node to the destination parent with the given name."""
        if not validate_name(final_name):
            return False

        if final_name in dest_parent.children:
            if dest_parent.children[final_name].is_directory:
                if source_node.is_directory:
                    print(f"Error: Directory '{final_name}' already exists in destination.")
                    return False
                dest_parent = dest_parent.children[final_name]
                final_name = source_node.name
            else:
                print(f"Error: File '{final_name}' already exists in destination.")
                return False

        # new node
        new_node = FileNode(
            name=final_name,
            is_directory=source_node.is_directory,
            content=source_node.content
        )
        new_node.parent = dest_parent
        new_node.created_at = datetime.now()
        new_node.modified_at = datetime.now()

        # directory then recursively copy children
        if source_node.is_directory:
            for child_name, child_node in source_node.children.items():
                if not copy_node(child_node, new_node, child_name):
                    return False
        dest_parent.children[final_name] = new_node
        return True