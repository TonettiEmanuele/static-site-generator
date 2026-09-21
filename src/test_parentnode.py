import unittest
from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_tag(self):
        node = ParentNode("tag", [], {})
        self.assertEqual(node.tag, "tag")

    def test_value(self):
        node = ParentNode("tag", [], {})
        self.assertEqual(node.value, None)

    def test_children(self):
        children: list[HTMLNode] = [LeafNode("h3", "I'm a child!")]
        node = ParentNode("tag", children, {})
        self.assertEqual(node.children, children)

    def test_props(self):
        children: list[HTMLNode] = [LeafNode("h3", "I'm a child!")]
        props = {"a": 1, "b": 2, "c": 3}
        node = ParentNode("tag", children, props)
        self.assertEqual(node.props, props)

    def test_props_none(self):
        children: list[HTMLNode] = [LeafNode("h3", "I'm a child!")]
        node = ParentNode(tag="tag", children=children)
        self.assertEqual(node.props, None)

    def test_parent_to_html(self):
        li_nodes: list[HTMLNode] = [
            ParentNode("li", [LeafNode("h1", "First heading")]),
            ParentNode("li", [LeafNode("h2", "Second heading")]),
            ParentNode("li", [LeafNode("h3", "Third heading")]),
        ]
        ul_node = ParentNode("ul", li_nodes)
        result = "<ul><li><h1>First heading</h1></li><li><h2>Second heading</h2></li><li><h3>Third heading</h3></li></ul>"
        self.assertEqual(ul_node.to_html(), result)
