'''To check if the given two BST are identical or not
We use the recursive approach where we check whether the value of the current node is equal or not
If it is, we then check whether the left and right subtrees are identical or not using recursion
If all the three conditions are true, BSTs are identical
Otherwise they are not
'''

class BSTNode:
    def __init__(self, data):
        self.val = data
        self.right = None
        self.left = None

def checkIdentical(bst1, bst2):
    #if bst2 is none and bst1 is not, then return false
    if bst1 and not bst2:
        return False
    #similar as above step
    if bst2 and not bst1:
        return False
    #if bst1 and bst2 are both None, then return true(identical)
    if not bst1 and not bst2:
        return True
    
    while bst1 and bst2:
        if bst1.val == bst2.val and checkIdentical(bst1.left, bst2.left) and checkIdentical(bst1.right, bst2.right):
            return True
        else:
            return False

def insertNode(root, value):
    if root is None:
        return BSTNode(value)
    if root.val == value:
        return root
    if root.val < value:
        root.right = insertNode(root.right, value)
    else:
        root.left = insertNode(root.left, value)

    return root

if __name__ == "__main__":
    bst1 = None
    bst2 = None
    flag = False
    res1 = input("Want to enter nodes in BST1?(y/n)")
    if res1 == "y" or res1 == "Y":
        while not flag: # this condition gets true as (!False)
            node_value = int(input("Enter node value: "))
            bst1 = insertNode(bst1, node_value)
            res = input("Want to add more?(y/n)")
            # if the user wants to quit
            if res == 'n' or res == 'N':
                # setting the flag to True
                flag = True

    print(f"Current Flag Value: {flag}")               
    res2 = input("Want to enter nodes in BST2?(y/n)")
    if res2 == "y" or res2 == "Y":
        # setting the flag to false as, we have change the flag value above
        flag = False
        while not flag:
            node_value = int(input("Enter node value: "))
            bst2 = insertNode(bst2, node_value)
            res = input("Want to add more?(y/n)")
            # if the user wants to quit
            if res == 'n' or res == 'N':
                flag = True
    
    print("Checking if the BSTs are identical...")
    if checkIdentical(bst1, bst2):
        print("\nYesss! They are identical")
    else:
        print("\nOoops! They are not identical")