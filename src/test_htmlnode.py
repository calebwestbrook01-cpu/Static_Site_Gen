import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test(self):
        node = HTMLNode("p", "hello")
        self.assertEqual(repr(node), "p, hello, None, None")
        node2 = HTMLNode("a", "Boot.dev", None, {"href": "https://boot.dev"})
        self.assertEqual(node2.props_to_html(), ' href="https://boot.dev"')

if __name__ == "__main__":
    unittest.main()