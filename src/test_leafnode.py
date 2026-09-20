import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_tag(self):
        node = LeafNode("tag", "value", {})
        self.assertEqual(node.tag, "tag")

    def test_value(self):
        node = LeafNode("tag", "value", {})
        self.assertEqual(node.value, "value")

    def test_children(self):
        node = LeafNode("tag", "value", {})
        self.assertEqual(node.children, None)

    def test_props(self):
        props = {"a": 1, "b": 2, "c": 3}
        node = LeafNode("tag", "value", props)
        self.assertEqual(node.props, props)

    def test_props_none(self):
        node = LeafNode(tag="tag", value="value")
        self.assertEqual(node.props, None)

    def test_leaf_to_html(self):
        props = {"href": "https://www.google.com"}
        node = LeafNode("a", "Click me!", props)
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )
