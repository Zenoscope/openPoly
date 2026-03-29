
#
# Linked List
#

# define a node structure for the list
class Node:
    def __init__(self, value=None):
        self.value = value # data item
        self.next = None # refernce to the next node

class List:
    def __init__(self):
        self.head = None # reference to the first node in the list

    # display the linked list
    def display(self):
        this_node = self.head #start of the list
        # iterate through each node until no next node is found
        print('{')
        node_number = 0
        while this_node is not None:
            print (f'Node {node_number} = {this_node.value}')
            this_node = this_node.next
            node_number += 1
        print('}')

    # add a node to the end of the list
    def append(self, node):
        if(self.head is None):
           # if this is the first node we are adding then it will become the head node
           self.head = node
        else:
          this_node = self.head
          # iterate through each node until no next node is found
          while this_node.next is not None:
            this_node = this_node.next
          # list will be the last node in our list, so, point it's next to the new node
          this_node.next = node

    # insert a node into the list
    def insert(self, node, index):
        if index == 0:
           node.next = self.head
           self.head = node
        else:
           # find the correct location to insert at
           position = 1
           this_node = self.head
           while position != index:
              position += 1
              this_node = this_node.next

           node.next = this_node.next
           this_node.next = node

    # remove a node at an index
    def remove(self, index):
        if index == 0:
           self.head = self.head.next
        else:
           # find the correct location to insert at
           position = 1
           this_node = self.head.next
           last_node = self.head
           while position != index:
              last_node = this_node
              position += 1
              this_node = this_node.next

           last_node.next = this_node.next

    # clear the list
    def clear(self):
       self.head = None

list = List()
list.display()

print('Append')
list.append(Node(5))
list.append(Node(25))
list.display()

print('Insert')
list.insert(Node(75), 1)
list.insert(Node(775), 0)
list.display()

print('Remove')
list.remove(1)
list.remove(0)
list.display()

print('Clear')
list.clear()
list.display()


add(self, PurchaseOrder,CustomerName)


"""
import csv
with open('Assessment_1_unsorted_orders.csv', mode ='r')as file:
    List list = new List()
    csvFile = csv.reader(file)
    count = 5

    for lines in csvFile:
        # print(lines)
        list.append(new Node(count *= 5));

    System.out.printf("The data in the list is:");
    list.display();
"""
