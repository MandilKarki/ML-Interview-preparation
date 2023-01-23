'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.


Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 or list2

        return dummy.next

'''
This code is an implementation of the mergeTwoLists function, which takes in two input lists (list1 and list2) and 
returns a new, merged list that contains all elements from both input lists in sorted order.

The function starts by creating a dummy node, which is an empty node that serves as a starting point for the merged list.
It also creates a pointer curr and sets it to the dummy node.

The function then enters a while loop that continues until both input lists are empty. Within the while loop, the function
compares the values of the first elements of both input lists (list1.val and list2.val) and appends the smaller value to
the merged list. The function then advances the pointer to the next node in the merged list, and the process continues.

Once one of the input lists is empty, the remaining elements of the non-empty list are appended to the merged list. Finally, 
the dummy node is returned as the head of the new merged list.

It's worth noting that, since we are using a dummy node to start the merged list, the result is returned from dummy.next.
This is because the dummy node is not part of the actual merged list, it is only used to start the construction of the merged
list.
'''