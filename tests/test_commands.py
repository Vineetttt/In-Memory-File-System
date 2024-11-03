import unittest
from src.core.file_system import FileSystem
from src.cli.command_parser import CommandParser

class TestCommands(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem()
        self.parser = CommandParser(self.fs)

    def test_mkdir(self):
        # simple directory
        self.parser.parse_and_execute("mkdir test_dir")
        self.assertIn("test_dir", self.fs.root.children)
        self.assertTrue(self.fs.root.children["test_dir"].is_directory)

        # nested directories
        self.parser.parse_and_execute("mkdir test_dir/nested_dir")
        self.assertIn("nested_dir", self.fs.root.children["test_dir"].children)

        # directory with invalid name
        self.parser.parse_and_execute("mkdir test_dir/invalid?dir")
        self.assertNotIn("invalid?dir", self.fs.root.children["test_dir"].children)

    def test_cd(self):
        # test directory
        self.parser.parse_and_execute("mkdir test_dir")
        
        # changing to directory
        self.parser.parse_and_execute("cd test_dir")
        self.assertEqual(self.fs.current_directory, self.fs.root.children["test_dir"])
        
        # changing to parent directory
        self.parser.parse_and_execute("cd ..")
        self.assertEqual(self.fs.current_directory, self.fs.root)
        
        # changing to non-existent directory
        self.parser.parse_and_execute("cd nonexistent")
        self.assertEqual(self.fs.current_directory, self.fs.root)

    def test_touch(self):
        # creating a file
        self.parser.parse_and_execute("touch test.txt")
        self.assertIn("test.txt", self.fs.root.children)
        self.assertFalse(self.fs.root.children["test.txt"].is_directory)
        
        # creating file in subdirectory
        self.parser.parse_and_execute("mkdir test_dir")
        self.parser.parse_and_execute("touch test_dir/nested.txt")
        self.assertIn("nested.txt", self.fs.root.children["test_dir"].children)