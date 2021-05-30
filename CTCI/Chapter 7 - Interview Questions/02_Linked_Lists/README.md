### Linked List:
A linked list is a data structure that represnts a sequence of nodes. In a singly linked list, each node points to the next node in the linked list.
A doubly linked list gives each node pointers to both the next node and the previous node. Unlike an array, a linked list does not provide constant
time access to a particular "index" within the list. This means that if you'd like to find the Kth element in the list, you will need to iterate
through K elements.
The benefit of a linked list is that you can add and remove items from the beginning of the list in constant time.

#### The "Runner" Technique:
The "runner" (or second pointer) technique is used in many linked list problems. The runner technique means that you iterate
through the linked list with two pointers simultaneously, with one ahead of the other. The "fast" node might be ahead by a fixed
amount, or it might be hopping multiple nodes for each one node that the "slow" node iterates through.

For example, suppose you had a linked list a1-> a2->...->an->b1->b2->...->bn and you wanted to rearrange it into
a1->b1->a2->b2->...->an->bn. You do not know the length of the linked list (but you do not know that the length is an even number).

You could have one pointer p1 (the fast pointer) move every two elements for every one move that p2 makes. When p1 hits the
end of the linked list, p2 will be at the midpoint. Then, move p1 back to the front and begin "weaving" the elements. On each
iteration, p2 selects an element and inserts it after p1.
