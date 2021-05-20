#Level order Travelsal of a tree

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class Tree:
    def __init__(self, root):
        self.root = TreeNode(root)

    def levelOrderTraversal(self, root):
        Visited = [root]
        path = " "
        while len(Visited) > 0:
            node = Visited.pop(0)
            if node.left:
                Visited.append(node.left)
            if node.right:
                Visited.append(node.right)
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
    tree.root.right.right = TreeNode(7)

    #Level Order Traversal : Every node at the same level is traversed before moving to the next level (BFS)
    print(tree.levelOrderTraversal(tree.root))
    