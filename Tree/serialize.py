class Node:
    def __init__(self,value):
        self.key = value
        self.left = None
        self.right = None

class String:
    def serialize(self,root):
        if root is None:
            return 'X'
        leftSubtree = self.serialize(root.left)
        rightSubtree = self.serialize(root.right)
        return root.key ","+ leftSubtree + ',' + rightSubtree

