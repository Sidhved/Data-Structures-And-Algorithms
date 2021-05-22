'''
COUNT OF LEAF NODES IN BINARY SEARCH TREE
Leaf node is a node which does not have left or right child
Number of leaf nodes varies with the order in which nodes are inserted
Time Complexity O(n)
'''

# Declare treeNode with data, right child (rc) and left child (lc)
from types import DynamicClassAttribute


class treeNode:
    def __init__(self, item):
        self.data = item
        self.lc = None
        self.rc = None

#to insert a node into BST
def insertIntoTree(root, data):
    #if tree is empty
    if root is None:
        root = treeNode(data)
    else:
        #insert recursively in accordance with BST properties
        if root.data >= data:
            root.lc = insertIntoTree(root.lc, data)
        elif root.data < data:
            root.rc = insertIntoTree(root.rc, data)
    return root

#to count the leaf nodes
def leaf_nodes(root):
    #if tree is not empty
    if root is not None:
        #if the node doesn't have any child increment count
        if root.lc is None and root.rc is None:
            leaf_nodes.count += 1
        else:
            #recursively check left and right sub-trees
            if root.lc is not None:
                leaf_nodes(root.lc)
            if root.rc is not None:
                leaf_nodes(root.rc)
    return leaf_nodes.count

#driver code
if __name__ == "__main__":
    root = None
    for _ in range(int(input("ENter the number of Elements: "))):
        root = insertIntoTree(root, int(input()))
        leaf_nodes.count = 0
        print(f"\nNumber of leaf nodes in the Binary Search Tree = {leaf_nodes(root)}")