### Linked List:
A linked list is a data structure that represnts a sequence of nodes. In a singly linked list, each node points to the next node in the linked list.
A doubly linked list gives each node pointers to both the next node and the previous node. Unlike an array, a linked list does not provide constant
time access to a particular "index" within the list. This means that if you'd like to find the Kth element in the list, you will need to iterate
through K elements.
The benefit of a linked list is that you can add and remove items from the beginning of the list in constant time.

#### Creating a Linked List:
```python
class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node
    
    def insert_at_tail(lst, value):
        # Creating a new node
        new_node = Node(value)

        # Check if the list is empty, if it is simply point head to new node
        if lst.get_head() is None:
            lst.head_node = new_node
            return

        # if list not empty, traverse the list to the last node
        temp = lst.get_head()

        while temp.next_element:
            temp = temp.next_element

        # Set the nextElement of the previous node to new node
        temp.next_element = new_node
        return


class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None
```

#### Deleting a Node from a singly Linked List:
```python
def delete(lst, value):
    deleted = False
    if lst.is_empty():  # Check if list is empty -> Return False
        print("List is Empty")
        return deleted
    current_node = lst.get_head()  # Get current node
    previous_node = None  # Get previous node
    if current_node.data == value:
        lst.delete_at_head()  # Use the previous function
        deleted = True
        return deleted

    # Traversing/Searching for Node to Delete
    while current_node is not None:
        # Node to delete is found
        if value == current_node.data:
            # previous node now points to next node
            previous_node.next_element = current_node.next_element
            current_node.next_element = None
            deleted = True
            break
        previous_node = current_node
        current_node = current_node.next_element

    if deleted == False:
        print(str(value) + " is not in list!")
    else:
        print(str(value) + " deleted!")

    return deleted
```

#### The "Runner" Technique:
The "runner" (or second pointer) technique is used in many linked list problems. The runner technique means that you iterate
through the linked list with two pointers simultaneously, with one ahead of the other. The "fast" node might be ahead by a fixed
amount, or it might be hopping multiple nodes for each one node that the "slow" node iterates through.

For example, suppose you had a linked list a1-> a2->...->an->b1->b2->...->bn and you wanted to rearrange it into
a1->b1->a2->b2->...->an->bn. You do not know the length of the linked list (but you do not know that the length is an even number).

You could have one pointer p1 (the fast pointer) move every two elements for every one move that p2 makes. When p1 hits the
end of the linked list, p2 will be at the midpoint. Then, move p1 back to the front and begin "weaving" the elements. On each
iteration, p2 selects an element and inserts it after p1.
