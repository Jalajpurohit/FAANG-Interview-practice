'''
Problem Statement:
Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

Hint 1: What if you knew the linked list size? What is the difference between finding the Kth-to-last element and
        finding the Xth element?
Hint 2: If you don't know the linked list size, can you compute it? How does it impace the runtime?
Hint 3: Try implementing it recursively. If you could find the (K-1)the to last element, can you find the Kth element?
Hint 4: You might find it useful to return multiple values. Some languages don't directly support this, but there are
        workarounds in essentially any language. What are some of those workarounds?
Hint 5: Can you do it iteratively? Imagine if you had two pointers pointing to the adjacent nodes and they were moving
        at the same speed through the linked list. When one hits the end of the linked list, where will the other be?
'''

from 02_Linked_Lists.linked_list import LinkedList


def kth_to_last(ll, k):
    runner = current = ll.head
    for _ in range(k):
        if not runner:
            return None
        runner = runner.next

    while runner:
        current = current.next
        runner = runner.next

    return current


test_cases = (
    # list, k, expected
    ((10, 20, 30, 40, 50), 1, 50),
    ((10, 20, 30, 40, 50), 5, 10),
)


def test_kth_to_last():
    for linked_list_values, k, expected in test_cases:
        ll = LinkedList(linked_list_values)
        assert kth_to_last(ll, k).value == expected


if __name__ == "__main__":
    test_kth_to_last()
