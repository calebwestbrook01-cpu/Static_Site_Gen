import unittest
from textnode import TextNode, TextType
from node_delimiter import split_nodes_delimiter

class TestNodeDelimiter(unittest.TestCase):
    def test_text(self):
        node = TextNode("It makes **more** sense than I expected", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("It makes ", TextType.TEXT),
            TextNode("more", TextType.BOLD),
            TextNode(" sense than I expected", TextType.TEXT)])