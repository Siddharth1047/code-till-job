# Reverse a LinkedList

class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

class Solution():
    def reverseList(self, head):
        prev = None
        current = head

        while current != None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
    
        head = prev
        return head

# Function to print the linked list
def printList(head):
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Creating a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Original linked list:")
printList(head)

# Creating an instance of Solution class
sol = Solution()

# Reversing the linked list
new_head = sol.reverseList(head)

print("Reversed linked list:")
printList(new_head)

# Problem 2(https://practice.geeksforgeeks.org/problems/linked-list-insertion-1587115620/1?page=1&difficulty[]=-1&difficulty[]=0&category[]=Linked%20List&sortBy=submissions)

"""
Create a link list of size N according to the given input literals. Each integer input is accompanied by an indicator which can either be 0 or 1. If it is 0, insert the integer in the beginning of the link list. If it is 1, insert the integer at the end of the link list. 
Hint: When inserting at the end, make sure that you handle NULL explicitly.

Example 1:

Input:
LinkedList: 9->0->5->1->6->1->2->0->5->0
Output: 5 2 9 5 6
Explanation:
Length of Link List = N = 5
9 0 indicated that 9 should be
inserted in the beginning. Modified
Link List = 9.
5 1 indicated that 5 should be
inserted in the end. Modified Link
List = 9,5.
6 1 indicated that 6 should be
inserted in the end. Modified Link
List = 9,5,6.
2 0 indicated that 2 should be
inserted in the beginning. Modified
Link List = 2,9,5,6.
5 0 indicated that 5 should be
inserted in the beginning. Modified
Link List = 5,2,9,5,6. 
Final linked list = 5, 2, 9, 5, 6.

Example 2:

Input:
LinkedList: 5->1->6->1->9->1
Output: 5 6 9
"""
# class Node is already created

class Solution1:

    def insertFirst(self, head, x):
        new_node = Node(x)
        new_node.next = head
        head = new_node
        return head
    
    def insertLast(self, head, x):
        new_node = Node(x)
        if head is None:
            head = new_node
            return head
        else:
            current = head
            while current.next != None:
                current = current.next
            current.next = new_node
            return head
        
#Driver Code (From GFG)
# Driver code
if __name__ == '__main__':
    # Taking input of the linked list
    arr = input().split()
    N = len(arr)
    head = None
    sol = Solution1()

    # Loop through the input literals
    for i in range(0, N, 2):
        x = int(arr[i])
        indicator = int(arr[i + 1])

        # If indicator is 0, insert at the beginning
        if indicator == 0:
            head = sol.insertFirst(head, x)
        # If indicator is 1, insert at the end
        elif indicator == 1:
            head = sol.insertLast(head, x)

    # Print the final linked list
    current = head
    while current is not None:
        print(current.data, end=" ")
        current = current.next
# Input = 9 0 5 1 6 1 2 0 5 0
# Output = 5 2 9 5 6



