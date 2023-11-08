class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1, l2):
    dummy_head = ListNode(-1)
    current = dummy_head

    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # Append the remaining elements from l1 or l2, if any
    while l1 is not None:
        current.next = l1
        l1 = l1.next
    while l2 is not None:
        current.next = l2
        l2 = l2.next

    return dummy_head.next


# Define nodes for the first linked list: 1 -> 2 -> 4
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(9)

# Define nodes for the second linked list: 1 -> 3 -> 5
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(5)
merged_list = mergeTwoLists(l1, l2)
current = merged_list
while current is not None:
    print(current.val, end=" -> ")
    current = current.next
