'''
Binary Search Tree : It is a binary tree
-> left element < root
-> right element > root

key concepts : 
-> inorder traversal is the sorted form of the elements
-> insert - O(log n)
-> search - O(log n)
-> delete - O(log n)
-> worst - O(n) (skewed tree)

1) inserting an element : logic : if data < root    -> add left
                                  else : add right if data > root


'''
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,root,data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left,data)
        else:
            root.right = self.insert(root.right,data)
        return root
    
    def search(self,root,key):
        if root is None or root.data == key:
            return root
        if key < root.data:
            return self.search(root.left,key)
        else:
            return self.search(root.right,key)
        
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)
    
    def find_min(self,root):
        while root.left:
            root = root.left
        return root
    
    def delete(self,root,key):
        if root is None:
            return root
        if key < root.data:
            root.left = self.delete(root.left,key)
        elif key > root.data:
            root.right = self.delet(root.right,key)
        else:
            #case-1: No child
            if root.left is None and root.right is None:
                return None
            #case-2: One child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            #case-3: two children
            temp = self.find_min(root.right)
            root.data = temp.data
            root.right = self.delete(root.right,temp.data)
        return root
bst = BST()
values = [10,5,15,2,7,12,20]
for v in values:
    bst.root = bst.insert(bst.root,v)
print("Inorder Traversal (Sorted):")
bst.inorder(bst.root)

print("\n search 7:","Found"if bst.search(bst.root,7)else "Not Found")

print("\n Deleting 10....")
bst.root = bst.delete(bst.root,10)

print("Inorder After Deletion:")
bst.inorder(bst.root)
