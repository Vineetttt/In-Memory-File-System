from datetime import datetime

class FileNode:
    def __init__(self, name, is_directory=False, content=""):
        self.name = name
        self.is_directory = is_directory
        self.content = content
        self.children = {}
        self.parent = None
        self.created_at = datetime.now()
        self.modified_at = datetime.now()