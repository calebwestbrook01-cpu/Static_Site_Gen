import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("LEARN TO CODE", TextType.BOLD)
        node2 = TextNode("Death by numbers", TextType.ITALIC)
        node3 = TextNode("Dial Up", TextType.PLAIN, "spotify.com")
        self.assertNotEqual(node, node2, node3)


if __name__ == "__main__":
    unittest.main()