''' Name: Ben Gertz
    Course: CMPS 1500
    Lab Section: Tuesday 5-6.15 PM
    Assignment: Lab 6 Part 2
    Date: 10/30/2017
    This program contains two functions for sorting the numbers in a file and outputting a new one, along with their corresponding sorting functions. It also
    has a program to create files with n random numbers for testing. This program also prints the runtime of the input, sorting, output, and total times for
    either sorting function.
'''
import time
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
    
def analyze_mergesort(inputfile, outputfile):
    '''
    This function uses the merge_sort() function to take numbers in a file, sort them and output them to another given
    file. It also prints the runtime of the input, output, sort, and total parts of the program.
    input: file with numbers -> file with sorted numbers, run times
    '''
    start = time.time()
    int_list = []
    start_read = time.time()
    f = open(inputfile, 'r')
    string_list = f.readlines()
    f.close()
    end_read = time.time()
    total_values = len(string_list)
    for num in range(len(string_list)):
        int_list.append(int(string_list[num]))
    start_sort = time.time()
    sorted_list = merge_sort(int_list)
    end_sort = time.time()
    start_write = time.time()
    g = open(outputfile, 'w')
    for index in sorted_list:
        g.write('%s\n' % index)
    g.close()
    end_write = time.time()
    end = time.time()
    print('It took', round((end_read - start_read), 6), 'seconds to input', total_values, 'values from file', inputfile)
    print('It took', round((end_sort - start_sort), 6), 'seconds to sort', total_values, 'values using merge sort')
    print('It took', round((end_write - start_write), 6), 'seconds to output', total_values, 'sorted values to file', outputfile)
    print('Total time the program took is', round((end - start), 6), 'seconds')

def analyze_selection(inputfile, outputfile):
    '''
    This function uses the selection_sort() function to take numbers in a file, sort them and output them to another given
    file. It also prints the runtime of the input, output, sort, and total parts of the program.
    input: file with numbers -> file with sorted numbers, run times 
    '''
    start = time.time()
    int_list = []
    start_read = time.time()
    f = open(inputfile, 'r')
    string_list = f.readlines()
    f.close()
    end_read = time.time()
    total_values = len(string_list)
    for num in range(len(string_list)):
        int_list.append(int(string_list[num]))
    print('It took', round((end_read - start_read), 6), 'seconds to input', total_values, 'values from file', inputfile)
    start_sort = time.time()
    sorted_list = selection_sort(int_list)
    end_sort = time.time()
    start_write = time.time()
    g = open(outputfile, 'w')
    for index in sorted_list:
        g.write('%s\n' % index)
    g.close()
    end_write = time.time()
    end = time.time()
    print('It took', round((end_read - start_read), 6), 'seconds to input', total_values, 'values from file', inputfile)
    print('It took', round((end_write - start_write), 6), 'seconds to output', total_values, 'sorted values to file', outputfile)
    print('It took', round((end_sort - start_sort), 6), 'seconds to sort', total_values, 'values using selection sort')
    print('Total time the program took is', round((end - start), 6), 'seconds')
   

def generate_nums(filename, n):
    '''
    This function creates a file with n random numbers 0- 99.
    input: filename and integer -> file with n random numbers
    '''
    f = open(filename, 'w')
    for num in range(n):
        f.write(str(random.randint(0, 99)) + '\n')
    f.close()
generate_nums('in10.txt', 10)
generate_nums('in100.txt', 100)
generate_nums('in1000.txt', 1000)
generate_nums('in10000.txt', 10000)
generate_nums('in100000.txt', 100000)
generate_nums('in1000000.txt', 1000000)



analyze_selection('input1000000.txt', 'testpart3.txt')


