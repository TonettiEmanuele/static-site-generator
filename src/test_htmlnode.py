import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_tag(self):
        node = HTMLNode("tag", "value", [], {})
        self.assertEqual(node.tag, "tag")

    def test_tag_none(self):
        node = HTMLNode(value="value", children=[], props={})
        self.assertEqual(node.tag, None)

    def test_value(self):
        node = HTMLNode("tag", "value", [], {})
        self.assertEqual(node.value, "value")

    def test_value_none(self):
        node = HTMLNode(tag="tag", children=[], props={})
        self.assertEqual(node.value, None)

    def test_children(self):
        child = HTMLNode("child")
        node = HTMLNode("tag", "value", [child], {})
        self.assertIsNotNone(node.children)
        if node.children is not None:
            self.assertIn(child, node.children)
        else:
            self.assertTrue(False)

    def test_children_none(self):
        node = HTMLNode(tag="tag", value="", props={})
        self.assertEqual(node.children, None)

    def test_props(self):
        props = {"a": 1, "b": 2, "c": 3}
        node = HTMLNode("tag", "value", [], props)
        self.assertEqual(node.props, props)

    def test_props_none(self):
        node = HTMLNode(tag="tag", value="value", children=[])
        self.assertEqual(node.props, None)

    def test_props_to_html(self):
        props = {"a": 1, "b": 2, "c": 3}
        node = HTMLNode("tag", "value", [], props)
        self.assertEqual(node.props_to_html(), 'a="1" b="2" c="3"')
