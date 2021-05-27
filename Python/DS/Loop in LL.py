'''Given a linked list, the task is to find whether the linked list consist of loop or not
The user will enter the elements in a linked list and will specify whether the tail of the linked list is pointed to some other node or Null
If the tail is pointing to Null, the user will input -1 in 'pos' variable, otherwise the user will input the index of the node to which the tail pointer will point
'pos'variable is only used to create a linked list as per the data entered by the user, it is not passed to the function for detecting a loop, it is being detected by using Floyd's cycle detection algorithm'''
#Time complexity O(n), Space Complexity O(1)
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.var  = None        #var pointer

    def push(self, newval):
        newNode = Node(newval)
        if self.var:
            self.var.next = newNode
            self.var = newNode
        else:
            self.head = newNode
            self.var = newNode
        return newNode
    
    def CreateLoop(self, idx, last):
        temp = self.head
        if idx >= 0:
            while idx>=0:
                temp = temp.next
                idx -= 1
            last.next = temp

    def LoopDetect(self):
        slow = self.head
        fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                print("Loop Detected!")
                return
        print("Loop not found!")

if __name__ == "__main__":
    n = int(input("Enter the size of the linked list: "))
    l1 = LinkedList()
    print("Enter Elements: ")
    for i in range(n):
        tail = l1.push(int(input()))

pos = int(input("Index of node which is connected to tail, else enter -1: "))
l1.CreateLoop(pos, tail)
l1.LoopDetect()