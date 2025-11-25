class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Subclasses must implement to_html()")

    def props_to_html(self):
        if not self.props:
            return ""
        parts = []
        for key, val in self.props.items():
            parts.append(f'{key}="{val}"')
        return " " + " ".join(parts)

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value")
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")

        # Raw text if no tag
        if self.tag is None:
            return self.value

        # Tagged HTML
        props_html = self.props_to_html()
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("ParentNode must have a tag")
        if children is None:
            raise ValueError("ParentNode must have children")

        if not isinstance(children, list):
            raise ValueError("Children must be a list")

        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")

        if self.children is None:
            raise ValueError("ParentNode must have children")

        # Render all children recursively
        inner_html = ""
        for child in self.children:
            inner_html += child.to_html()

        props_html = self.props_to_html()
        return f"<{self.tag}{props_html}>{inner_html}</{self.tag}>"
