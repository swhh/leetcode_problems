"""Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.



Example 1:


Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
Example 2:


Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]


Constraints:

The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106"""

# Definition for singly-linked list.


test_head1 = [1, 2, 3, 4, 5]
test_output1 = [1, 3, 5, 2, 4]

test_head2 = [2, 1, 3, 5, 6, 4, 7]
test_output2 = [2, 3, 6, 7, 1, 5, 4]


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def odd_even_list(head):
    current = head
    first_even = head.next
    odd = True
    last_odd = head

    while current:
        neighbor = current.next
        if neighbor:
            current.next = neighbor.next
        if odd:
            last_odd = current
        current = neighbor
        odd = not odd
    last_odd.next = first_even
    return head


def map_list_to_linked_list(nums):
    previous_node = None
    for num in nums[::-1]:
        node = ListNode(val=num, next=previous_node)
        previous_node = node
    return node


def map_linked_list_to_list(head):
    nums = []
    current = head
    while current:
        nums.append(current.val)
        current = current.next
    return nums


def test():
    test_nodes1 = map_list_to_linked_list(test_head1)
    test_nodes2 = map_list_to_linked_list(test_head2)
    output1 = odd_even_list(test_nodes1)
    output2 = odd_even_list(test_nodes2)
    assert map_linked_list_to_list(output1) == test_output1
    assert map_linked_list_to_list(output2) == test_output2


if __name__ == '__main__':
    test()
