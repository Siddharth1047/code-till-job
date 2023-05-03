# Merge 2 Linked Lists in a sorted manner

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        replicate = ListNode()
        curr = replicate

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = list1 or list2
        return replicate.next
    
# Example usage:
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)

# Print the merged list
while merged_list:
    print(merged_list.val, end=" ")
    merged_list = merged_list.next

# Merge 2 arrays in a sorted manner

def mergeArrays(arr1, arr2):
    merged_array = arr1 + arr2
    merged_array.sort()
    return merged_array

# Example:
arr1 = [1,3,5,7]
arr2 = [1,2,4,6,9]
print(mergeArrays(arr1, arr2))