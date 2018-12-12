'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single
digit.Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        elif l2 == None:
            return l1

        remain = 0
        l = ListNode(None)
        result = l

        while l1 != None or l2 != None:
            if l1 == None:
                l1 = ListNode(0)
            elif l2 == None:
                l2 = ListNode(0)
            total = l1.val + l2.val + remain
            if total >= 10:
                total = total - 10
                remain = 1
            else:
                remain = 0
            l.next = ListNode(total)
            l1 = l1.next
            l2 = l2.next
            l = l.next
        if remain == 1:
            l.next = ListNode(remain)

        return result.next


if __name__ == '__main__':

    num1 = [2,4,3]
    num2 = [5,6,4]
    ###初始化l1
    l1 = ListNode(num1[0])
    cur1 = l1
    for i in num1[1:]:
        node = ListNode(i)
        cur1.next = node
        cur1 = cur1.next

    ###初始化l2
    l2 = ListNode(num2[0])
    cur2 = l2
    for i in num2[1:]:
        node = ListNode(i)
        cur2.next = node
        cur2 = cur2.next


    s = Solution()
    rst = s.addTwoNumbers(l1,l2)

    cur = rst
    while cur:
        print(cur.val)
        cur = cur.next