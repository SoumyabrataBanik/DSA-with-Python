# Create the node class:
class Node:
    def __init__(self, value: int):
        self.data = value
        self.next = None


# Create the Singly Linked List Class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Create the Append method of the class
    def append(self, value: int):
        # Check if the head is empty? If it is then create a new node at the head with the value provided
        if self.head is None:
            self.head = Node(value)
            return

        # If the head is not empty, then create a dummy node (current_node) and store the head in it.
        current_node = self.head
        # Traverse the linked list using while loop. We can also use the for loop if we use the length method defined
        # below.
        while current_node.next is not None:
            current_node = current_node.next
        # Once we have found the end of the list, append the new value to the list.
        current_node.next = Node(value)

    # Define the show_elements function that will display the linked list.
    def show_elements(self):
        # Create a dummy node (current_node) and store the head node in it.
        current_node = self.head
        # traverse the linked list using the while loop.
        while current_node is not None:
            # Each time we encounter a new node, print it.
            print(current_node.data, end='->')
            # Update the dummy node to point to the next element.
            current_node = current_node.next

    # Define the length method that will provide us the length of the linked list
    def length(self) -> int:
        # Create a variable that will work as a counter.
        result: int = 0
        # Create a dummy node (current_node) and store the head node in it.
        current_node = self.head
        # Traverse the linked list until you reach the end
        while current_node is not None:
            # Increase the counter by one each time you move to a new node.
            result += 1
            # Update the dummy node to point to the next node in the linked list
            current_node = current_node.next
        return result

    # Define the search method that will search for a value in the linked list
    def search(self, value: int) -> bool:
        # Create a dummy node and store the head node in it.
        current_node = self.head
        # Traverse the linked list until you reach the end.
        while current_node is not None:
            # If you find the value in the linked list return true
            if current_node.data is value:
                return True
            # Update the dummy node to point to the next node in the linked list.
            current_node = current_node.next
        # If the value was not found, return false.
        return False

    # Define the remove method that will delete a value from the linked list
    def remove(self, value: int) -> None:
        # Check if the linked list is empty? If it is, then just return!
        if self.head is None:
            return

        # If the linked list is not empty, then follow the below lines.

        # Check if the value is the very first value in the linked list. If it is, then update the head node to point
        # to the next node and return.
        elif self.head.data == value:
            self.head = self.head.next
            return

        # If the value is not the first value in the linked list, create a dummy node and store the head node in it.
        current_node = self.head
        # Create a node that will keep track of the previous node.
        previous_node = None

        # Traverse the linked list until you reach the end:
        while current_node is not None:
            # If you find the value
            if current_node.data == value:
                # Point the previous_node to the next node, ignoring the current node
                previous_node.next = current_node.next
                return
            # If the value is not found, move to the next node. Make sure to point the previous node to the current node
            previous_node = current_node
            current_node = current_node.next


def main() -> None:
    linkedlist = SinglyLinkedList()
    option: int = 0

    while option < 5:
        print("\n\n1. Add a value \n2. Print the linked list \n3. Search for a value \n4. Delete a value from the "
              "list \n5. Quit")
        option = int(input("Choose an option: "))
        if option == 1:
            linkedlist.append(int(input("Enter the value to add to the list: ")))
        elif option == 2:
            linkedlist.show_elements()
        elif option == 3:
            if linkedlist.search(int(input("Enter the value to search for in the list: "))):
                print("Value found in the linked list")
            else:
                print("Value not found in the linked list")
        elif option == 4:
            linkedlist.remove(int(input("Enter the value to be deleted from the linked list: ")))
        elif option == 5:
            print("Quitting the program...")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()
