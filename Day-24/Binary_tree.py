'''
Binary Tree: A binary tree is a hierarchical data structure in which each node has 
at most two children. 

Types of Binary Trees:
1) Full Binary Tree: A binary tree in which every node has either 0 or 2 children.
2) Complete Binary Tree: A binary tree in which all levels are completely filled except 
last and child aligned to the left.
3) Perfect Binary Tree: A binary tree in which all levels are completely filled
4) Balanced Binary Tree: Height approximately log(n)
5) Skewed Binary Tree: It is like a linked list, where each node has only one child.

Basic problems on Binary Tree:
1) count the number of nodes in a binary tree: 
    Formula : 1+count(left subtree) + count(right subtree)
2) height of a binary tree: count of levels from root node to the deepest leaf node
    Formula : 1+max(height(left subtree) , height(right subtree))
3) counting leaf nodes in a binary tree: 
    Formula : count(left subtree) + count(right subtree) 
4) Level order traversal: 
    visit nodes level by level from left to right
  
 
'''

from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def count_leaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)

def level_order(root):
    if root is None:
        return
    q = deque({root})
    
    while q:
        node = q.popleft()
        print(node.data, end=" ")

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("total nodes:", count_nodes(root))
    print("height :",height(root))
    print("leaf nodes:", count_leaves(root))
    print("level order:")
    level_order(root)
main()
