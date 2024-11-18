class Node:
   def __init__(self,data):
       self.data = data
       self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end = "->")
            current = current.next
        print("None")

    def remove(self, data):
        current = self.head
        prev = None

        # Case 1: If the list is empty
        if not current:
            print("The list is empty.")
            return

        # Case 2: If the data is in the head node
        if current.data == data:
            new_head = current.next
            current.next = None  # Disconnect the node
            self.head = new_head
            return

        # Case 3: Traverse to find the node to remove
        while current and current.data != data:
            prev = current
            current = current.next

        # Case 4: If the data is not found
        if not current:
            print(f"{data} is not present in the linked list.")
            return

        # Case 5: Remove the node by bypassing it
        prev.next = current.next
        current.next = None  # Disconnect the node








