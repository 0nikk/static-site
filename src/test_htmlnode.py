import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_no_props(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")
    
    def test_props_to_html_one_prop(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')
    
    def test_props_to_html_multiple_props(self):
        node = HTMLNode(
            props={
                "href": "https://www.google.com",
                "target": "_blank"
            }
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"'
        )
    
    def test_repr(self):
        node = HTMLNode(
            tag="div",
            value="hello",
            children=[HTMLNode(tag="p", value="child")],
            props={"class": "greeting"}
        )
        expected = 'HTMLNode(tag=div, value=hello, children=[HTMLNode(tag=p, value=child, children=None, props=None)], props={\'class\': \'greeting\'})'
        self.assertEqual(repr(node), expected)

if __name__ == "__main__":
    unittest.main() 