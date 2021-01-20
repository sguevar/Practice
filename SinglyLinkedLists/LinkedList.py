class Node:
    def __init__(self, data):          # When using the Node class, data is a parameter and there is no next initially
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):                # Initially, the Linked List is empty so None is the head of the linked list
        self.head = None

    def append(self, data):            # append data creates a new node that uses data as a parameter for the Node class
        new_node = Node(data)
        if self.head is None:          # if the Linked List is empty, then make the new Node that we appended the head.
            self.head = new_node
            return
        last_node = self.head               # Start from the beginning and make our way down the list
        while last_node.next:               # While the next node is not empty
            last_node = last_node.next      # Make the last node variable the next node since it is not empty
        last_node.next = new_node           # Once we get to the end of the Linked list, make the next node our new Node

    def prepend(self, data):                        # Append to the front of the list
        new_node = Node(data)
        new_node.next = self.head                   # Make the node next be the rest of the list and put it in the front
        self.head = new_node

    def print_linked_list(self):
        current = self.head                  # Start from the beginning
        while current:                       # While there is not a None
            print(current.data)              # Print the data from the Node and then make the current node the next node
            current = current.next

    def insert_after_node(self, prev_node, data):
        if not prev_node:                    # Checks if the prev_node is in the LinkedList, if not then returns nothing
            print("Node not found, enter a valid Node")
        new_node = Node(data)  # The new node will contain everything after the prev node and the prev node will contain
        new_node.next = prev_node.next  # the new node as its next
        prev_node.next = new_node

    def delete_node(self, key):

        current = self.head

        if current and current.data == key:   # We are looking to see if the head is the key we are deleting
            self.head = current.next          # If so, the head becomes the next node and the old head is turned to None
            current = None
            return

        prev = None
        while current and current.data != key:  # If the key is not the same as the current Node, then the prev variable
            prev = current                      # saves the data of the old node until we reach the node we need to
            current = current.next              # delete, then the next node of the prev variable is everything after
                                                # the current element which will be deleted
        if current is None:
            return

        prev.next = current.next
        current = None

    def delete_by_pos(self, pos):                  # Takes in pos
        if self.head:                              # if the head is not empty, then store the head in current
            cur_node = self.head
            if pos == 0:
                self.head = cur_node.next          # If pos == 0, it means we are deleting the head, so make the head
                cur_node = None                    # curr_node.next, which stores everything except the head and
                return                             # make the head None

            prev = None
            count = 0
            while cur_node and count != pos:      # The while loop will end when we reach the end of the linked list
                prev = cur_node                   # or if count is equal to pos, which means we reached the node we need
                cur_node = cur_node.next          # We are storing each node, one by one until we delete the node at pos
                count += 1

            if cur_node is None:
                return

            prev.next = cur_node.next
            cur_node = None

    def iter_length(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

    def recursion_length(self,node):
        if node is None:
            return 0
        return 1 + self.recursion_length(node.next)


lst1 = LinkedList()
lst1.append("A")
lst1.append("B")
lst1.append("C")
lst1.delete_node("C")
lst1.prepend("D")
lst1.delete_by_pos(0)
lst1.insert_after_node(lst1.head.next, "E")
print(lst1.iter_length())
print(lst1.recursion_length(lst1.head))
lst1.print_linked_list()
