class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    # Add a child to this node
    def insert(self, value):
        # First check whether our value is greater or lesser
        if (self.value > value):
            # If lesser, then it needs to be inserted to the left
            if self.left is None:
                self.left = Node(value)
                return self.left
            return self.left.insert(value)

        # Otherwise, insert to the right
        if self.right is None:
            self.right = Node(value)
            return self.right
        return self.right.insert(value)

    # Display this node and its children
    def display(self, level, spaces_per_level):
        space = ' ' * level
        if spaces_per_level > 0:
            print(f'{space}{self.value}')
        if self.left is not None:
            self.left.display(level + spaces_per_level, spaces_per_level)
        if spaces_per_level == 0:
            print(self.value)
        if self.right is not None:
            self.right.display(level + spaces_per_level, spaces_per_level)

class BinaryTree:
  def __init__(self):
      self.root = None

  def insert(self, value):
    if self.root is None:
      self.root = Node(value)
      return self.root

    return self.root.insert(value)

  def display(self, spaces_per_level):
    if (self.root is not None):
      self.root.display(0, spaces_per_level)

"""
tree = BinaryTree()
tree.insert('Hamilton')
tree.insert('Wellington')
tree.insert('Christchurch')
tree.insert('Dunedin')
tree.insert('Napier')
tree.insert('Palmerston North')
tree.insert('Masterton')

print('Flat display')
print('============')
tree.display(0)

print()
print('Indented display')
print('================')
tree.display(2)
"""


import csv
with open('Assessment_1_unsorted_orders.csv', mode ='r')as file:
    tree = BinaryTree()
    csvFile = csv.reader(file)
    for lines in csvFile:
        # print(lines)
        add(self, PurchaseOrder,CustomerName)
        tree.insert(lines)

    print('Flat display')
    print('============')
    tree.display(0)

    print()
    print('Indented display')
    print('================')
    tree.display(2)


