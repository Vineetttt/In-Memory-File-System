def normalize_path(path):
    """Normalize a file system path."""
    if not path:
        return "."
    # Remove consecutive slashes
    while "//" in path:
        path = path.replace("//", "/")
    # Remove trailing slash unless it's root
    if path != "/" and path.endswith("/"):
        path = path[:-1]
    return path