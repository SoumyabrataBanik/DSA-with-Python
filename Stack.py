class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        return self.items == []

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return

    def get_stack(self):
        return self.items


def main():
    stack = Stack()
    option = 0

    while option < 7:
        print("\n1. Push item into the stack. \n2. Pop item from the stack. \n3. Peek at topmost item in the stack. "
              "\n4. Check if the stack is empty. \n5. Display Stack. \n6. Quit")
        option = int(input("Enter your choice: "))

        if option == 1:
            stack.push(input("Enter the item to push into the stack: "))

        elif option == 2:
            print(stack.pop())

        elif option == 3:
            print(stack.peek())

        elif option == 4:
            print(stack.is_empty())

        elif option == 5:
            print(stack.get_stack())

        elif option == 6:
            print("Exiting the program...")
            break

        else:
            print("Invalid Choice. Choose a proper option.")


if __name__ == "__main__":
    main()