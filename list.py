# Laboratory Work: Linked List Implementation

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Delete node by key
    def delete_node(self, key):
        temp = self.head

        # If head node itself holds the key
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        # Search for the key
        prev = None
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # If key was not present
        if temp is None:
            print(f"Key {key} not found in list.")
            return

        # Unlink the node
        prev.next = temp.next
        temp = None

    # Display the linked list
    def display_list(self):
        temp = self.head
        if temp is None:
            print("List is empty.")
            return
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")



# ------------------ Testing ------------------
if __name__ == "__main__":
    ll = LinkedList()

    # Insert 5 values
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_end(40)
    ll.insert_at_end(50)

    print("Linked List after inserting 5 values:")
    ll.display_list()

    # Insert at beginning
    ll.insert_at_beginning(5)
    print("\nAfter inserting 5 at beginning:")
    ll.display_list()

    # Delete one node
    ll.delete_node(30)
    print("\nAfter deleting node with value 30:")
    ll.display_list()
