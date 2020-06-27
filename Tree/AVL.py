class Node:
    def __init__(self,data):
        self.parent =None
        self.left=None
        self.right=None
        self.key = data

class AVL:
    def __init__(self):
        self.root=None
        self.currentSize=0
    
    def leftRotate(self,node):
        temp = node.right
        temp.parent = node.parent
        node.parent = temp
        node.right = temp.left
        temp.left = node
        return temp

    def rightRotate(self,node):
        temp = node.left
        temp.parent = node.parent
        node.parent = temp
        node.left = temp.right
        temp.right = node
        return temp

    def leftRightRotate(self,node):
        node.left = self.leftRotate(node.left)
        return self.rightRotate(node)

    def rightLeftRotate(self,node):
        node.right = self.rightRotate(node.right)
        return self.leftRotate(node)

    def height(self,node):
        if node is None:
            return 0
        else:
            lDepth = self.height(node.left)
            rDepth = self.height(node.right)
            if(lDepth>rDepth):
                return lDepth+1
            else:
                return rDepth+1


    def rebalance(self,node):
        if((self.height(node.left)-self.height(node.right))>1):
            if(self.height(node.left.left)>self.height(node.left.right)):
                print("rebalancing",node.key)
                node = self.rightRotate(node)
                if node.parent is not None:
                    print("parent node",node.parent.key)
            else:
                node = self.leftRightRotate(node)
        else:
            if((self.height(node.right.left)>self.height(node.right.right))):
                node = self.leftRotate(node)
            else:
                node = self.rightLeftRotate(node)

        if(node.parent==None):
            self.root = node
        print("rebalnce returns",node.key)
        return node 
    
    def checkBalance(self,node):
        if(abs(self.height(node.left)-self.height(node.right))>1):
            Parent = node.parent
            node = self.rebalance(node)
            node.parent = Parent
            return node
        else:
            if(node.parent==None):
                return 
            else:
                print("inside else in checkBalnce",node.parent.key)
                return self.checkBalance(node.parent)


    def add(self,parent,node):
        if(node.key>parent.key):
            if(parent.right==None):
                parent.right=node
                node.parent = parent
                self.currentSize+=1
            else:
                return self.add(parent.right,node)
        else:
            if(parent.left==None):
                parent.left=node
                node.parent=parent
                self.currentSize+=1
            else:
                return self.add(parent.left,node)
        print("======================",node.key,node.parent.key)
        return self.checkBalance(node)

    def insert(self,data):
        node = Node(data)
        if self.root == None:
            self.root = node
            self.currentSize+=1
        else:
            self.add(self.root,node)
    
    def levelOrderTraversal(self):
        temp = self.root
        queue=[]
        if self.root is None:
            return
        queue.append(self.root)
        while(len(queue)>0):
            print(queue[0].key)
            temp = queue.pop(0)
            if temp.left is not None:
                queue.append(temp.left)
            if temp.right is not None:
                queue.append(temp.right)


    def inorderTraversal(self):
        if node is not None:
            self.inorderTraversal()
            

if __name__ == '__main__':
    numbers = [10,9,8,7,6]
    avl = AVL()
    for num in numbers:
        avl.insert(num)
    print("Tree===============")
    avl.levelOrderTraversal()
    print("size",avl.currentSize)
