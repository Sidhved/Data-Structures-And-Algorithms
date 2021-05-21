'''Implementation of Binary Search Tree
Binary Search Tree is a special type of binary tree where:
1. The value of all the nodes in th eleft subtree is less than or equal to the value of the root
2. The value of all ht nodes to the right sub tree is greater than value of the root
3. This rule will be recursively applied to all the left and right subtrees of the root

Here we use a switch to operate different functionalities:
1. Insert Node in BST
2. Search Node in BST
3. Delete Node in BST
4. Print BST (inorder way)
'''

class BSTNode:
    #A node of the binary search tree
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def insertNode(root, val):
        if root is None:
            return BSTNode(val)

        if root.val == val:
            return root

        if root.val <= val:
            root.right = insertNode(root.right , val)

        else:
            root.left = insertNode(root.left, val)

        return root

def searchNode(root, val):
        if root is None:
            return False

        if root.val == val:
            return True

        if val >root.val:
            return searchNode(root.right, val)

        return searchNode(root.left, val)

def inorderSuccessor(node):
        curr = node
        #loop through the bst until left most node is reached
        while curr.left is not None:
            curr = curr.left
        return curr
    
def deleteNode(root, val):
        if root is None:
            return root
        
        if root.val > val:
            root.left = deleteNode(root.left, val)
        
        if root.val < val:
            root.right = deleteNode(root.right, val)

        else:
            #if the root has 1 child or no children
            if root.right is None:
                Node = root.left
                root = None
                return Node
            
            if root.left is None:
                Node = root.right
                root = None
                return Node

            #if the node has 2 children
            Node = inorderSuccessor(root.right)
            root.val = Node.val
            root.right = deleteNode(root.right, Node.val)
        return root

def inorder(root):
        if root:
            inorder(root.left)
            print(root.val, end = " ")
            inorder(root.right)

#driver method
if __name__ == "__main__":
    bst = None
    op = 1
    while op != 5:
        print("1 : Insert")
        print("2 : Search")
        print("3 : Delete")
        print("4 : Print(inorder)")
        print("5 : Exit")
        print("Enter Option: ", end=" ")
        op = int(input()) 

        if op == 1:
            print("Enter the value to insert: ")
            i = int(input())
            bst = insertNode(bst, i)

        elif op == 2:
            print("Enter element to search for: ")
            i = int(input())
            if searchNode(bst, i):
                print("Node Found")
            else:
                print("Node not found")

        elif op == 3:
            print("ENter the value to delete: ")
            i = int(input())
            bst.deleteNode(bst, i)

        elif op == 4:
            if bst:
                inorder(bst)
            else:
                print("The tree is empty")
