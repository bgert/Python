''' Name: Ben Gertz
    Course: CMPS 1500
    Lab Section: Tuesday 5-6.15 PM
    Assignment: Lab 9 Part 0
    Date: 11/20/2017
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)

def join(head1, head2):
    '''
    This function takes two list heads as input, adds the second list to the end of the first
    and returns the head of the new combined list.
    The Asymptotic run time of the function is O(n1) becuase the function to find the end of list one is ran
    as many times as there are nodes in n1, but the part of the function that adds the second list to the end
    of the first is not dependent on the size of n2 and is always O(1) therefore O(n1 + 1) simplifies to O(n1).
    '''
    def findEnd(head1):
        if head1.next == None:
            return head1
        else:
            return findEnd(head1.next)
    if head1 == None:
        return head2
    findEnd(head1).next = head2
    return head1

l1 = Node('a')
l1.next = Node('b')
l1.next.next = Node('c')
l2 = Node('d')
l2.next = Node('e')
l2.next.next = Node('f')
join(None, l2)


    
