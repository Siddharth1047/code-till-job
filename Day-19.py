# Check whether a BinaryTree is a BST or not.

class Node:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.left = None
        self.right = None

def treeMax(node):
    if node is None:
        return float("-inf")
    maxleft = treeMax(node.left)
    maxright = treeMax(node.right)
    return max(node.key, maxleft, maxright)

def treeMin(node):
    if node is None:
        return float("inf")
    minleft = treeMin(node.left)
    minright = treeMin(node.right)
    return max(node.key, minleft, minright)

def verify(node):
    if node is None:
        return True
    if treeMax(node.left) <= node.key <= treeMin(node.right) and verify(node.left) and verify(node.right):
        return True
    else:
        return False
    
root= Node(10, "Hello")
root.left = Node(5, "Five")
root.right= Node(30, "Thirty")

print(verify(root)) # prints True

root = Node(10, "Ten")
root.right = Node(20, "Twenty")
root.left = Node(5, "Five")
root.left.right = Node(15, "Fifteen")

print(verify(root)) # prints False
