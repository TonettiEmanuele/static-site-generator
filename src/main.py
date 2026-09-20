from textnode import TextNode, TextType
from htmlnode import HTMLNode


def main():
    node = TextNode("text", TextType.PLAIN)
    print(node)
    props = {"a": 1, "b": 2, "c": 3}
    html_node = HTMLNode("tag", "value", [], props)
    print(html_node)


if __name__ == "__main__":
    main()
