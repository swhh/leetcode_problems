"""Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
"""

linked_list_one  = [1,3,4,7,1,2,6]
linked_list_two = [1,2,3,4]

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_middle(head):
    """Delete middle node and return head of modified linked list"""
    list_length = 1
    current = head
    while current.next:
        list_length += 1
        current = current.next
    middle = list_length // 2
    current = past = head
    while middle:
        past = current
        current = current.next  
        middle -= 1
    past.next = current.next
    del current
    return head


def build_linked_list(linked_list: list):
    head = ListNode(val=linked_list[0])
    current = head
    for val in linked_list[1:]:
        current.next = ListNode(val=val)
        current = current.next
    return head

def build_list(head: ListNode):
    linked_list = []
    current = head
    while current:
        linked_list.append(current.val)
        current = current.next
    return linked_list

def test():
    head = build_linked_list(linked_list_one)
    head = delete_middle(head)
    new_linked_list = build_list(head)
    print(new_linked_list)
    middle = len(linked_list_one) // 2
    print(linked_list_one[:middle] + linked_list_one[middle + 1: ])
    assert linked_list_one[:middle] + linked_list_one[middle + 1: ] == new_linked_list

if __name__ == '__main__':
    test()
    
    
