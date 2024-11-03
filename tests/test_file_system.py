import unittest
from src.core.file_system import FileSystem
from src.core.file_node import FileNode

class TestFileSystem(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem()

    def test_init(self):
        self.assertIsNotNone(self.fs.root)
        self.assertTrue(self.fs.root.is_directory)
        self.assertEqual(self.fs.root.name, "/")
        self.assertEqual(self.fs.current_directory, self.fs.root)

    def test_get_node_by_path(self):
        # test root path
        self.assertEqual(self.fs._get_node_by_path("/"), self.fs.root)
        
        # test non-existent path
        self.assertIsNone(self.fs._get_node_by_path("/nonexistent"))
        
        # test nested path
        dir_node = FileNode("test_dir", is_directory=True)
        dir_node.parent = self.fs.root
        self.fs.root.children["test_dir"] = dir_node
        
        file_node = FileNode("test_file")
        file_node.parent = dir_node
        dir_node.children["test_file"] = file_node
        
        self.assertEqual(self.fs._get_node_by_path("/test_dir"), dir_node)
        self.assertEqual(self.fs._get_node_by_path("/test_dir/test_file"), file_node)
