# Find height of a tree

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

class Solution:
    def height(self, root):
        if root is None:
            return 0
        
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        
        return max(left_height, right_height) + 1 # '+1' for the subtree + rootNode
    
s = Solution()
print(s.height(root))
"""
Tree is: -
        1
       / \
      2   3
     / \
    4   5
"""

# Find if 2 given trees're identical or not

class Solution1:
    def isIdentical(self, root1, root2):
        if root1 is None and root2 is None:
            return True

        if root1 is None or root2 is None:
            return False

        if root1.data != root2.data:
            return False
        
        left_identical = self.isIdentical(root1.left, root2.left)
        right_identical = self.isIdentical(root1.right, root2.right)
        
        # Return True only if both left and right subtrees are identical
        return left_identical and right_identical
    
# Create two binary trees
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)

ss = Solution1()

# Check if the two trees are identical
if ss.isIdentical(root1, root2):
    print("Yes")
else:
    print("No")