''' Name: Ben Gertz
    Course: CMPS 1500
    Lab Section: Tuesday 5-6.15 PM
    Assignment: Lab 9 Part 1
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
    if head1 == None:
        return head2
    findEnd(head1).next = head2
    return head1

def findEnd(head1):
        if head1.next == None:
            return head1
        else:
            return findEnd(head1.next)
    
def add(lst, old, new):
    if len(lst) != 0:
        for i in range(len(lst)):
            if lst[i].data == old and lst[i].next.data == new:
                print('Entry already exists!')
                return False
        return True
    else:
        return True

def remove(lst, old, new):
    if len(lst) != 0:
        for i in range(len(lst)):
            if lst[i].data == old and lst[i].next.data == new:
                print('Removed!')
                return True
            print('No such entry!')
            return False
    else:
        print('No such entry!')
        return False
    
def isAddress(lst, address):
    if len(lst) != 0:
        for i in range(len(lst)):
            if lst[i].data == address:
                print('Send to', lst[i].next.data)
            else:
                print('Send to', address)
    else:
        print('Send to', address)
        
def get_menu_choice():
    choice = input()
    return str(choice)
choice = ''
lst = []
while choice != 'QUIT':
    choice = get_menu_choice()
    if choice == 'ADD':
        address1 = input()
        address2 = input()
        if add(lst, address1, address2) == True:
            address1 = Node(address1)
            address1.next = Node(address2)
            lst.append(address1)
            print('Added!')
    elif choice == 'REMOVE':
        address1 = input()
        address2 = input()
        if remove(lst, address1, address2) == True:
            for i in range(len(lst)):
                if lst[i].data == address1 and lst[i].next.data == address2:
                    lst.pop(i)
                else:
                    pass
            #print('Removed!')
    elif choice == 'Mail':
        address = input()
        isAddress(lst, address)
    for i in range(len(lst) - 1):
        if lst[-1].data == lst[i].next.data:
            lst[i].next = lst[-1]
            lst.pop(-1)
    for i in range(len(lst) - 1):
        if lst[-1].data == lst[i].data:
            lst.pop(i)
print('Goodbye')
