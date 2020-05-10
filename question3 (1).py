class Node: 
    def __init__(self, key): 
        self.left = None
        self.right = None
        self.val = key
def printpostorder(root): 
  
    if root: 
       # First recur on left child 
       printpostorder(root.left) 
  
       # the recur on right child 
       printpostorder(root.right)

       # now print the data of node 
       print(root.val)

root=Node('A')
root.left=Node('B')
root.right=Node('U')
root.left.left=Node('S')
root.left.right=Node('R')
root.right.left=Node('E')
root.right.right=Node('P')
root.left.left.left=Node('W')
root.left.right.left=Node('Y')
root.left.right.right=Node('X')
root.right.right.left=Node('G')
root.right.right.right=Node('J')
root.left.left.left.left=Node('z')

printpostorder(root)
