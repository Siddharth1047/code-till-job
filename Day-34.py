# Find Middle of a LinkedList
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_middle_node(head):
    slow_ptr = head
    fast_ptr = head

    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    return slow_ptr.data

# Driver code
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    middle_node = find_middle_node(head)
    print("Middle Node:", middle_node)
