"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
"""

 # Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


    def mergeTwoLists(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #Set the values ahead of time
        valuel1 = l1.val
        valuel2 = l2.val

        if valuel1 > valuel2:
            mergedList = ListNode(valuel2)
            mergedList.next = None
            valuel2 = valuel2.next
        if valuel1 < valuel2:
            mergedList = ListNode(valuel1)
            mergedList.next = None
            valuel1 = valuel1.next
        if valuel1 == valuel2:
            mergedList = ListNode(valuel1)
            mergedList.next = None
            valuel1 = valuel1.next  


        while l1 or l2:
            if valuel1 > valuel2:
                mergedList = ListNode(mergedList.next)
                mergedList.val = valuel2
                mergedList.next = None
                l2 = l2.next
                valuel2 = l2.val
            if valuel1 < valuel2:
                mergedList = ListNode(mergedList.next)
                mergedList.val = valuel1
                mergedList.next = None
                l1 = l1.next
            if valuel1 == valuel2:
                mergedList = ListNode(mergedList.next)
                mergedList.val = valuel1
                mergedList.next = None
                l1 = l1.next
          

                
            





def printLinkedList(node):
    while node:
        print(node.val)
        node = node.next



testL1Node1 = ListNode(2)
testL1Node2 = ListNode(4)
testL1Node3 = ListNode(6)
testL1Node4 = ListNode(8)

testL1Node1.next = testL1Node2
testL1Node2.next = testL1Node3
testL1Node3.next = testL1Node4


testL2Node1 = ListNode(1)
testL2Node2 = ListNode(3)
testL2Node3 = ListNode(5)
testL2Node4 = ListNode(7)

testL2Node1.next = testL2Node2
testL2Node2.next = testL2Node3
testL2Node3.next = testL2Node4


for i in range(10):
    testLinkedList = ListNode(i)
    print(testLinkedList.val)
    testLinkedList.next = ListNode(None)
    testLinkedList = testLinkedList.next

printLinkedList(testLinkedList)



#printLinkedList(testL1Node1)
#printLinkedList(testL2Node1)

#printLinkedList(ListNode.mergeTwoLists(testL1Node1, testL1Node2))