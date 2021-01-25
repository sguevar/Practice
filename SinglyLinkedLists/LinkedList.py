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

    def swap_node(self, node1, node2):
        if node1 == node2:                              # If the node are the same, then we do nothing so this is the
            return                                      # first case we should look for
        current = self.head
        prev = None
        while current and current.data != node1:        # If current node is not the one we are looking for, we save the
            prev = current                              # we save the old nodes and the current node moves forward
            current = current.next

        current_2 = self.head
        prev_2 = None
        while current_2 and current_2.data != node2:    # This also checks if we are not at the end of the linked list
            prev_2 = current_2
            current_2 = current_2.next

        if not current or not current_2:                # This checks if one of the nodes is missing in the linked list,
            return                                      # in this case we cannot swap

        if prev:                                        # If prev exists, it means current is not the head. We then swap
            prev.next = current_2                       # with the second node, if the current node was the head, then
        else:                                           # we swap by making the second node the head.
            self.head = current_2

        if prev_2:
            prev_2.next = current
        else:
            self.head = current

        current.next, current_2.next = current_2.next, current.next

    def reverse_iterative(self):
        prev = None                                     # We start with the head, for each current node, we store the
        current = self.head                             # next node of the current node. We then turn the next node into
        while current:                                  # the node before the current one. The previous node is now the
            nxt = current.next                          # current and the current node is now the next node we stored
            current.next = prev                         # in the beginning, the prev node is then turned into the head.
            prev = current
            current = nxt
        self.head = prev

    def recursive_reverse(self):                        # Make a method inside the method that deals with one case and
        def reverse(current, previous):                 # Use recursion to go through the entire list.
            if not current:                             # If we reach the end of the list, return the previous
                return previous
            next = current.next
            current.next = previous                     # Same thing as iterative method, this time we use recursion
            previous = current                          # Instead of a loop.
            current = next
            return reverse(current, previous)
        self.head = reverse(current=self.head, previous=None)

    def sorted_merge(self, llist):
        p1 = self.head
        p2 = llist.head
        q = None

        if not p1:
            return p2
        if not p2:
            return p1

        if p1 and p2:
            if p1.data <= p2.data:
                q = p1
                p1 = q.next
            else:
                q = p2
                p2 = q.next
            new_head = q
        while p1 and p2:
            if p1.data <= p2.data:
                q.next = p1
                q = p1
                p1 = q.next
            else:
                q.next = p2
                q = p2
                p2 = q.next
        if not p1:
            q.next = p2
        if not p2:
            q.next = p1
        return new_head

    def print_nth_from_last(self, n):
        total_len = self.len_iterative()            # We get the length, and remove 1 from the length
        cur = self.head                             # every time we go down a node until we reach the
        while cur:                                  # node we want
            if total_len == n:
                print(cur.data)
                return cur.data
            total_len -= 1
            cur = cur.next
        if cur is None:
            return

    def count_occurences_iterative(self, data):
        count = 0
        cur = self.head
        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next
        return count

    def rotate(self, k):
        if self.head and self.head.next:
            p = self.head
            q = self.head
            prev = None
            count = 0

            while p and count < k:
                prev = p
                p = p.next
                q = q.next
                count += 1
            p = prev
            while q:
                prev = q
                q = q.next
            q = prev

            q.next = self.head
            self.head = p.next
            p.next = None

    def is_palindrome(self):
        # Solution 2:
        p = self.head
        s = []
        while p:
            s.append(p.data)
            p = p.next
        p = self.head
        while p:
            data = s.pop()
            if p.data != data:
                return False
            p = p.next
        return True

lst1 = LinkedList()
lst2 = LinkedList()
lst1.append(1)
lst1.append(4)
lst1.append(6)
lst2.append(2)
lst2.append(3)
lst2.append(7)
lst2.append(10)
lst1.sorted_merge(lst2)
lst1.print_linked_list()

