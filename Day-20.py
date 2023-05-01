"""
Given a Tree: - 
        1
       / \
      2   3
     /   / \
    4    5  6

Print: -
1
2 3
4 5 6
"""
import collections

class Node:
    def __init__(self, key = None):
        self.key = key
        self.left = None
        self.right = None

def levelOnePrint(tree):
    if not tree:
        return False
    
    nodes = collections.deque([tree])
    currentcount = 1
    nextcount = 0

    while len(nodes) != 0:

        currentNode = nodes.popleft()
        currentcount -= 1

        print(currentNode.key, end=' ')

        if currentNode.left:
            nodes.append(currentNode.left)
            nextcount += 1

        if currentNode.right:
            nodes.append(currentNode.right)
            nextcount += 1

        if currentcount == 0:
            print()
            currentcount, nextcount = nextcount, currentcount

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
levelOnePrint(root)