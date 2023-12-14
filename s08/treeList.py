#We import default to map the tree depth and coordinates
from collections import defaultdict, deque
#Here we make a root node and also the main function to traverse the tree
class Node:
    #assign left, right nodes, list, datalink
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        self.arr = []
    def traverse(self):
        #this lines creates the dictionary for the tree we will be using
        main_Order = defaultdict(list)
        #this is a queue for the level order traversal
        queue = deque()
        #this line pairs both the current node and its coordinates in the tree
        queue.append((root,0))
        #This chunk traverses the dictionary
        while queue:
            node, depth = queue.popleft()
            main_Order[depth].append(node.data)
            if node.left:
                queue.append((node.left,depth-1))
            if node.right:
                queue.append((node.right,depth+1))
        #this line sorts the dictionary's keys accoring to its depth and order
        sort = sorted(main_Order.keys())
        #iterates through tree
        for depth in sort:
            #appends numbers to list
            self.arr.extend(main_Order[depth])
        #Reverses list to match output
        self.arr.reverse()
        #prints list
        return print(res)
#Make tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)

#call function
root.traverse()




