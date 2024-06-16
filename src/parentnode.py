from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)


    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode: tag not provided")
        if not self.children:
            raise ValueError("ParentNode: children not provided")
        return f"<{self.tag}>{''.join(map(lambda child: child.to_html(), self.children))}</{self.tag}>"
