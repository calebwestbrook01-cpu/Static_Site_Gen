import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMDToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
        md2 = """
_It's all italics baby_

**YOU WISH IT WAS BOLD**
"""
        blocks2 = markdown_to_blocks(md2)
        self.assertEqual(
            blocks2,
            [
                "_It's all italics baby_",
                "**YOU WISH IT WAS BOLD**",
            ]
        )