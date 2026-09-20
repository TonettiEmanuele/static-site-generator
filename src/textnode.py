from enum import Enum


class TextType(Enum):
    TEXT_PLAIN = "plain"
    TEXT_BOLD = "bold"
    TEXT_ITALIC = "italic"
    TEXT_CODE = "code"
    TEXT_LINK = "link"
    TEXT_IMAGE = "image"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str | None = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value: object, /) -> bool:
        if type(value) is TextNode:
            return (
                self.text == value.text
                and value.text_type == value.text_type
                and self.url == value.url
            )
        else:
            return False

    def __repr__(self) -> str:
        return f"TextType({self.text}, {self.text_type}, {self.url})"
