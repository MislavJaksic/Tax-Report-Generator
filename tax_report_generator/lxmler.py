from lxml import etree


class Lxmler:
    def __init__(self, xml_file_path):
        self.xml_file_path = xml_file_path
        self.tree = self.get_tree()
        self.root = self.get_tree_root()

    def get_tree(self):
        tree = etree.parse(self.xml_file_path)
        return tree

    def get_tree_root(self):
        root = self.tree.getroot()
        return root


class LxmlTreeRoot:
    def __init__(self, root):
        self.root = root


# to correct the file sum every column
#   to sum a column add up all nodes in the same column
#     to add an element take an element from the subtree
#       to take the subtree parse the tree
#         to parse the tree open the file
