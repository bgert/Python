''' Name: Ben Gertz
    Course: CMPS 1500
    Lab Section: Tuesday 5-6.15 PM
    Assignment: Lab 6 Part 2
    Date: 10/30/2017
    This program contains two functions for sorting the numbers in a file and outputting a new one, along with their corresponding sorting functions. It also
    has a program to create files with n random numbers for testing.
'''
import random
random.seed(0)

def selection_sort( aList ):
  """Sorts a list in ascending order using the selection sort algorithm.
  """
  n = len( aList )
  for i in range( n - 1 ):
    
      
    # Find the minimum element in the unsorted portion of the list
    
    smallNdx = i # assume the ith element is the smallest.
    
    # Determine if any other element contains a smaller value.
    for j in range( i + 1, n ):
      if aList[ j ] < aList[ smallNdx ] :
        smallNdx = j

    # Swap the ith value and smallNdx value  
                      
    tmp = aList[ i ]
    aList[ i ] = aList[ smallNdx ]
    aList[ smallNdx ] = tmp

  return aList

def merge_sort( aList ):
    """
    Merge sort recursively divide the list into half, sort both halves
    and then merge the two sorted lists into one.
    """
    # If the aList is size 0 or 1, it's already sorted.
    if len( aList ) <= 1:
        return aList

    else:
        mid = len( aList ) // 2

        # Recursively sort the left and right halves
        left = merge_sort( aList[ :mid ] )
        right = merge_sort( aList[mid:] )
        
        # Merge the two (each sorted) parts back together
        return merge( left, right )


                                
def merge( left, right ):
    """
    Merge to sorted list, left and right, into one sorted list.
    """
    aList = []
    lt = 0
    rt = 0

    # Repeatedly move the smallest of left and right to the new list
    while lt < len( left ) and rt < len( right ):
        if left[ lt ] < right[ rt ]:
            aList.append( left[ lt ]  )
            lt += 1
        else:
            aList.append( right[ rt ] )
            rt += 1

    # There will only be elements left in one of the original two lists.

    # Append the remains of left (lt..end) on to the new list.
    while lt < len(left):
        aList.append( left[ lt ] )
        lt += 1
         
    # Append the remains of right (rt..end) on to the new list.
    while rt < len( right ):
        aList.append( right[ rt ] )
        rt += 1

    return aList
    
def use_mergesort(inputfile, outputfile):
    '''
    This function uses the merge_sort() function to take numbers in a file, sort them and output them to another given
    file. input: file with numbers -> file with sorted numbers
    '''
    int_list = []
    f = open(inputfile, 'r')
    string_list = f.readlines()
    f.close()
    for num in range(len(string_list)):
        int_list.append(int(string_list[num]))
    sorted_list = merge_sort(int_list)
    g = open(outputfile, 'w')
    for index in sorted_list:
        g.write('%s\n' % index)
    g.close()

def use_selection(inputfile, outputfile):
    '''
    This function uses the selection_sort() function to take numbers in a file, sort them and output them to another given
    file. input: file with numbers -> file with sorted numbers
    '''
    int_list = []
    f = open(inputfile, 'r')
    string_list = f.readlines()
    f.close()
    for num in range(len(string_list)):
        int_list.append(int(string_list[num]))
    sorted_list = selection_sort(int_list)
    g = open(outputfile, 'w')
    for index in sorted_list:
        g.write('%s\n' % index)
    g.close()

def generate_nums(filename, n):
    '''
    This function creates a file with n random numbers 0- 99.
    input: filename and integer -> file with n random numbers
    '''
    f = open(filename, 'w')
    for num in range(n):
        f.write(str(random.randint(0, 99)) + '\n')
    f.close()
