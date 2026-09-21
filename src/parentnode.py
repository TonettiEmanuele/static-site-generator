from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(
        self, tag: str, children: list["HTMLNode"], props: dict | None = None
    ) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("missing tag")
        if self.children is None or len(self.children) < 1:
            raise ValueError("children not set")
        else:

            def to_html_func(child):
                return child.to_html()

            html_children = "".join(map(to_html_func, self.children))
            if self.props is None:
                return f"<{self.tag}>{html_children}</{self.tag}>"
            else:
                return (
                    f"<{self.tag} {self.props_to_html()}>{html_children}</{self.tag}>"
                )

    def __repr__(self):
        output = "HTMLNode(\n"
        output += f"\ttag={self.tag}\n"
        output += f"\tvalue={self.value}\n"
        output += f"\tprops={self.props}\n"
        output += ")"
        return output
