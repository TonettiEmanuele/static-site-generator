from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict | None = None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError()
        if self.tag is None:
            return self.value
        else:
            if self.props is None or len(self.props) < 1:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        output = "HTMLNode(\n"
        output += f"\ttag={self.tag}\n"
        output += f"\tvalue={self.value}\n"
        output += f"\tprops={self.props}\n"
        output += ")"
        return output
