'''
Problem Statement:
Partition - Write code to partition a linked list around a value X, such that all nodes less than X come before all nodes
            greated than or equal to X. If X is contained within the list, the values of X only need to be after the elements
            less than X. The partition element X can appear anywhere in the "right partition". It does not need to appear
            between the left and right partitions.

Example:
Input     - 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
Output    - 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

Hint 1: There are many solutions to this problem, most of which are equally optimal in runtime. Some have shorter,
        cleaner code than others. Can you brainstorm different solutions?
Hint 2: Consider that the elements don't have to stay in the same relative order. We only need to ensure that elements
        less than the pivot must be before elements greater than the pivot. Does that help you come up with more solutions?
'''

from 02_Linked_Lists.linked_list import LinkedList


def partition(ll, x):
    current = ll.tail = ll.head

    while current:
        next_node = current.next
        current.next = None
        if current.value < x:
            current.next = ll.head
            ll.head = current
        else:
            ll.tail.next = current
            ll.tail = current
        current = next_node

    # Error check in case all nodes are less than x
    if ll.tail.next is not None:
        ll.tail.next = None


def example():

    ll = LinkedList.generate(10, 0, 99)
    print(ll)
    partition(ll, ll.head.value)
    print(ll)


if __name__ == "__main__":
    example()
