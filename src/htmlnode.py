class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list["HTMLNode"] | None = None,
        props: dict | None = None,
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self) -> str:
        if self.props is None:
            return ""
        else:
            lines: list[str] = []
            for tag in self.props:
                lines.append(f'{tag}="{self.props[tag]}"')
            return " ".join(lines)

    def __repr__(self):
        output = "HTMLNode(\n"
        output += f"\ttag={self.tag}\n"
        output += f"\tvalue={self.value}\n"
        output += f"\tchildren={self.children}\n"
        output += f"\tprops={self.props}\n"
        output += ")"
        return output
