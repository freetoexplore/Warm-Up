# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        l1_new = []
        leng1 = 0
        for i in l1:
            leng1 += 1

        for i in range(leng1):  
            l1_new.append(l1[-1])
            del l1[-1]

        l2_new = []
        leng2 = 0
        for i in l2:
            leng2 += 1

        for i in range(leng2):  
            l2_new.append(l2[-1])
            del l2[-1]

        for i in range(leng1):  
            l1_new.append(l1[-1])
            del l1[-1]

        ini_sum1 = 0
        for i in l1_new:
            ini_sum1 += 10**(leng1 - 1)*i
            l1_new = [k for k in l1_new if k != i]


        for i in range(len(l2)):  
            l2_new.append(l2[-1])
            del l2[-1]

        ini_sum2 = 0
        for i in l2_new:
            ini_sum2 += 10**(leng2 - 1)*i
            l2_new = [k for k in l2_new if k != i]

        l3 = [i for i in str(ini_sum1 + ini_sum2)]

        l3_new = []
        leng3 = 0
        for i in l3:
            leng3 += 1

        for i in range(leng3):  
            l3_new.append(int(l3[-1]))
            del l3[-1]
            
        print(l3_new)