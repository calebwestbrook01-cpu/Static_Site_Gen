import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("LEARN TO CODE", TextType.BOLD)
        node2 = TextNode("Death by numbers", TextType.ITALIC)
        node3 = TextNode("Dial Up", TextType.TEXT, "spotify.com")
        self.assertNotEqual(node, node2, node3)
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()