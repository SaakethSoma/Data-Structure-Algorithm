'''
Trees: A tree is a data structure that consists of nodes connected by edges. 
It is a hierarchical structure that represents relationships between different elements. 

Node : Basic element of a tree that contains data and may have child nodes.
Each node in a tree can have zero or more child nodes

Root node : It is one special node called the root node that serves as the starting point of the tree.
Edge : An edge is a connection between two nodes in a tree.
Parent: A node that has one or more child nodes is called a parent node.
Child: A node that is connected to a parent node is called a child node.    
Leaf: A node that does not have any child nodes is called a leaf node.
Sibling: Nodes that share the same parent node are called siblings.
Height: Longest path from the root node to a leaf node is called the height of the tree.

Why we use trees? 
-> we use trees to represent hierarchical data, Fast searching and insertion needed
used in : File systems, databases, AI(decision trees,Random Forests)

1)Inorder Traversal: Left, Root, Right
2)Preorder Traversal: Root, Left, Right
3)Postorder Traversal: Left, Right, Root

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
#traversal Functions
#inorder(left -> root-> right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

#preorder(root -> left -> right)
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)
#postorder(left -> right -> root)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

def main():
    #create nodes
    root = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    #connect nodes
    root.left = node2
    root.right = node3

    node2.left = node4
    node2.right = node5

    print("Inorder Traversal: ")
    inorder(root)

    print("\nPreorder Traversal: ")
    preorder(root)

    print("\nPostorder Traversal: ")
    postorder(root)

main()