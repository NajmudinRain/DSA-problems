class Node:
    def __init__(self, data):  # Corrected the constructor
        self.data = data
        self.prev = None
        self.next = None


class Doubly_LL:
    def __init__(self):  # Corrected the constructor
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        temp = self.head
        while temp.next:  # Traverse to the last node
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def delete_node(self, key):
        temp = self.head
        while temp:  # Traverse to find the node with the given key
            if temp.data == key:
                # Adjust pointers for the previous node
                if temp.prev:
                    temp.prev.next = temp.next
                else:  # If it's the first node
                    self.head = temp.next
                # Adjust pointers for the next node
                if temp.next:
                    temp.next.prev = temp.prev
                del temp  # Free the memory for the deleted node
                return
            temp = temp.next
        print(f"Node with data {key} not found.")  # Key not found

    def traverse_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" --> ")
            temp = temp.next
        print("None")

    def traverse_backward(self):
        temp = self.head
        if not temp:  # If the list is empty
            print("List is empty.")
            return
        # Traverse to the last node
        while temp.next:
            temp = temp.next
        # Traverse backward
        while temp:
            print(temp.data, end=" --> ")
            temp = temp.prev
        print("None")


obj = Doubly_LL()
for i in range(10):
    obj.insert_at_end(i)

obj.delete_node(5)
obj.traverse_forward()
obj.traverse_backward()
















