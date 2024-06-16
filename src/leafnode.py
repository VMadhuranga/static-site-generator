from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value=None, props=None):
        super().__init__(tag, value, None, props)

    
    def to_html(self):
        if not self.value and self.tag != "img":
            raise ValueError("LeafNode: all leaf nodes require a value")
        if not self.tag:
            return self.value
        if not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
