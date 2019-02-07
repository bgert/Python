''' Name: Ben Gertz
    Course: CMPS 1500
    Lab Section: Tuesday 5-6.15 PM
    Assignment: Lab 10 Part 0
    Date: 12/4/2017
    This program contains a class Node and a function getheight(root) that determines the height of a bst.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def getheight(root):
    if root == None:
        return 0
    else:
        x = getheight(root.left)
        y = getheight(root.right)
        if x == 0 and y == 0:
            return 1
        elif y == x:
            return 1 + y
        elif y > x:
            return 1 + y
        elif x > y:
            return 1 + x

def getheight(root):
    '''
    This function takes the head of a BST and returns its height.
    '''
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 0
    else:
        x = getheight(root.left)
        y = getheight(root.right)

        if y == x:
            return 1 + y
        elif y > x:
            return 1 + y
        elif x > y:
            return 1 + x
