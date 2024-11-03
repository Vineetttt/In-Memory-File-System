import unittest
from src.core.file_system import FileSystem
from src.cli.command_parser import CommandParser

class TestFileOperations(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem()
        self.parser = CommandParser(self.fs)

    def test_echo_and_cat(self):
        # writing to file
        self.parser.parse_and_execute('echo "Hello, World!" > test.txt')
        self.assertIn("test.txt", self.fs.root.children)
        
        # reading from file
        file_content = self.fs.root.children["test.txt"].content  
        self.assertEqual(file_content, "Hello, World!")

    def test_cp_and_mv(self):
        # test file
        self.parser.parse_and_execute('echo "Test Content" > source.txt')
        
        # test copy
        self.parser.parse_and_execute("cp source.txt dest.txt")
        self.assertIn("dest.txt", self.fs.root.children)
        self.assertEqual(
            self.fs.root.children["source.txt"].content,
            self.fs.root.children["dest.txt"].content
        )
        
        # test move
        self.parser.parse_and_execute("mv source.txt moved.txt")
        self.assertNotIn("source.txt", self.fs.root.children)
        self.assertIn("moved.txt", self.fs.root.children)