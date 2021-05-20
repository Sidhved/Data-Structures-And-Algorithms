#creating Node class to frame a single node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#creating a linked list class to get all the helper functionalities inside
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        if self.tail is None:
            self.head = Node(data)
            self.tail = self.head

        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end = " ")
            temp = temp.next

#creating a solution class to implement more methods on the Linked List
class Solution:
    def length(self, head):
        temp = head
        count = 0
        while(temp):
            temp = temp.next
            count += 1
        return count

    #recursive approach to reverse linked list
    def reverse_linked_list(self, head):
        #if head or head.next is null
        if (head is None or head.next is None):
            return head

        #getting small output using recursion
        small_head = self.reverse_linked_list(head.next)
        head.next = None

        #traversing to the end node
        temp = small_head
        while(temp.next is not None):
            temp = temp.next

        #putting the head pointerat the next of end node
        temp.next = head
        head = small_head
        return head
    
    #the iterative approach to reverse the linked list
    def reverse_linked_list_iterative(self, head):
        #if head or its next pointer is null
        if (head is None or head.next is None):
            return head
        '''getting 3 pointers, prev = to store the previous pointer
                               temp = auxiliary storage (Node pointer)
                               curr = current pointer'''

        prev = None
        curr = head

        while(curr):
            temp = curr.next
            curr.next = prevprev = curr
            curr = temp
        return prev

#driver code
if __name__ == "__main__":
    LL = LinkedList()
    LL.head = Node(1)

    #taking inputs using map and list
    arr = list(map(int, input().split()))

    #forging the linked list
    for i in arr:
        LL.append(i)
    LL.printList()
    sol = Solution()

    #recursive approach
    LL1 = LinkedList()
    LL1.head = sol.reverse_linked_list(LL.head)
    LL1.printList()

    #iterative approach
    LL2 = LinkedList()
    LL2.head = sol.reverse_linked_list_iterative(LL.head)
    LL2.printList()