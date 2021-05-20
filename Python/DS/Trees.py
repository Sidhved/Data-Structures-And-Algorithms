#Program to traverse given tree in pre-order, in-order and post-order fashion

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root):
        self.root = TreeNode(root)

    def inorderTraversal(self, node, path):
        if node:
            path = self.inorderTraversal(node.left, path)
            path += str(node.val) + " "
            path = self.inorderTraversal(node.right, path)
        return path
    
    def preorderTraversal(self, node, path):
        if node:
            path += str(node.val) + " "
            path = self.preorderTraversal(node.left, path)
            path = self.preorderTraversal(node.right, path)
        return path

    def postorderTraversal(self, node, path):
        if node:
            path = self.postorderTraversal(node.left, path)
            path = self.postorderTraversal(node.right, path)
            path += str(node.val) + " "
        return path

'''lets construct a binary tree as shown below to understand with help of an example
        1
      /   \
     2     3
   /  \   /  \
 4     5 6    7
'''

if __name__ == "__main__":
    tree = Tree(1)
    tree.root.left = TreeNode(2)
    tree.root.right = TreeNode(3)

    tree.root.left.left = TreeNode(4)
    tree.root.left.right = TreeNode(5)
    tree.root.right.left = TreeNode(6)
    tree.root.right.left = TreeNode(7)

    #In-Order Traversal : left -> root -> right
    print(tree.inorderTraversal(tree.root, " "))

    #Pre-order Traversal : root -> left -> right
    print(tree.preorderTraversal(tree.root, " "))

    #Post-order Traversal : left -> right -> root
    print(tree.postorderTraversal(tree.root, " "))