import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a text noooode", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_textType(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.PLAIN)
        self.assertNotEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "url")
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("Text", TextType.PLAIN)
        self.assertEqual(node.text, "Text")

    def test_textType(self):
        node = TextNode("Text", TextType.BOLD)
        self.assertEqual(node.text_type, TextType.BOLD)

    def test_link_none(self):
        node = TextNode("Text", TextType.PLAIN)
        self.assertEqual(node.url, None)

    def test_link_value(self):
        node = TextNode("Text", TextType.LINK, "link")
        self.assertEqual(node.url, "link")


if __name__ == "__main__":
    unittest.main()
