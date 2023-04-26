# Implement a BinaryTree

class BinaryTree(object):

    # initialise the structure of a tree
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        # if leftChild has no value, insert a newNode
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            # if it has a value, then push the existing node below and add a newNode for the current node
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        # if rightChild has no value, insert a newNode
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            # if it has a value, then push the existing node below and add a newNode for the current node
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getLeftChild(self):
        return self.leftChild 

    def getRightChild(self):
        return self.rightChild

    def setRootVal(self, obj):
        self.key = obj # set a root node

    def getRootVal(self):
        return self.key
    
    def _inorderTraversal(self, node):
        if node is not None:
            self._inorderTraversal(node.getLeftChild())
            print(node.getRootVal(), end=" ")
            self._inorderTraversal(node.getRightChild())

# Create a binary tree
myTree = BinaryTree("A")
myTree.insertLeft("B")
myTree.insertRight("C")
myTree.getLeftChild().insertLeft("D")
myTree.getLeftChild().insertRight("E")
myTree.getRightChild().insertLeft("F")
myTree.getRightChild().insertRight("G")

# Print the entire tree
print("Binary Tree: ", end="")
myTree._inorderTraversal(myTree)
# Output: D B E A F C G
"""
        A
       / \
      B   C
     / \ / \
    D  E F  G
"""