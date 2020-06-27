class Node:
    def __init__(self,value):
        self.key = value
        self.left = None
        self.right = None


class BST:
    def insert(self,root,value):
        if(root == None):
            root = Node(value)
        elif(value>root.key):
            root.right = self.insert(root.right,value)
        elif(value<root.key):
            root.left = self.insert(root.left,value)
        return root

    def search(self,root,value):
        if(root == None):
            return None
        elif(root.key == value):
            return root
        elif(value>root.key):
            return self.search(root.right,value)
        else:
            return self.search(root.left,value)


    def minValue(self,root):
        temp = root
        while(temp.left!=None):
            temp = temp.left
        return temp

    def delete(self,root,value):
        if root is None:
            return root
        elif(value>root.key):
            root.right = self.delete(root.right,value)
        elif(value<root.key):
            root.left = self.delete(root.left,value)
        else:
            if root.left is None and root.right is None:
                root = None
            elif(root.left is None):
                root = root.right
            elif(root.right is None):
                root = root.left
            else:
                temp = self.minValue(root.right)
                root.key = temp.key
                root.right = self.delete(root.right,temp.key)
            return root
        return root


    def preorder(self,root):
        if root is not None:
            print(root.key)
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key)

    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print(root.key)
            self.inorder(root.right)



if __name__ == '__main__':
    bst = BST()
    root = None
    root = bst.insert(root,50)
    root = bst.insert(root,70)
    root = bst.insert(root,30)
    root = bst.insert(root,80)
    root = bst.insert(root,60)
    root = bst.insert(root,40)
    root = bst.insert(root,20)
    print("++++++++print preorder++++++++")
    bst.preorder(root)
    print("-------postorder--------------")
    bst.postorder(root)
    print("---------inorder--------------")
    bst.inorder(root)
    print("After deleting 30")
    bst.delete(root,30)
    bst.inorder(root)
