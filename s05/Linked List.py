class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = Node(data)


        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next:
                if current.data < current.next.data:
                    savedata = current.data
                    current.data = current.next.data
                    current.next.data = savedata

                current = current.next

            current.next = new_node

    def display(self):
        current = self.head
        while(current):
            print(current.data, end=" -> ")
            current = current.next
        print("None")

input_values = [6,3,4,2,1]
my_linked_list = LinkedList()

for value in input_values:
    my_linked_list.insert(value)

my_linked_list.display()

