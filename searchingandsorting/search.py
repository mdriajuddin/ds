# unsorted linearSearch

def linearSearch(theValues, target):
    n = len(theValues)
    for i in range(n):
        # if the target is in the ith element, return True
        if theValues[i] == target:
            return True
    return False


# sortedLinearSearch

def sortedLinearSearch(theValues, item):
    n = len( theValues)
    for i in range(n):
        # If the target is found in the ith element, return True
        if theValues[i] == item:
            return True
        # If target is larger than the ith element, it's not in the sequence.
        elif theValues[i] > item:
            return False
    return False   # The item is not in the sequence.


# find Smallest 
def dindSmallest(theValues):
    n = len( theValues)
    # Assume the first item is the smallest value.
    smallest = theValues[0]
    # Determine if any other item in thet sequence is smaller.
    for i in range(1, n):
        if theList[i] < smallest:
            smallest = theValues[i]
    return smallest   # Return the smallest found.
    


def binarySearch(theValues, target):
    # Start with the entire sequence of elements.
    low = 0
    high = len(theValues) - 1

    # Repeatedly subdivide the sequence in half until the target is found.
    while low <= high:
        # Find th midpoint of the sequence.
        mid = (high + low) // 2
        # Does the midpoint contain the target?
        if theValues[mid] == target:
            return True
        # Or does the target precede the midpoint?
        elif target < theValues[mid]:
            high = mid - 1
        # Or does ite follow the midpoint?
        low = mid + 1
    # If the sequence cannot be subdivided further, we're done.
    return False









# Modified version of the binary search that returns the index within
# a sorted sequence indication where the target the should be located.
def findSortedPosition(theList, target):
    low = 0
    high = len(theList) - 1
    while low <= high:
        mid = (high + low ) // 2
        if theList[mid] == target:
            return mid          # Index of the terget.
        elif target < theList[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return low              # Index where the target value should be.

# Mearges toe sorted lists to create and return a new sorted list.
def mergeSortedLists( listA, listB):
    # Creates the nre list and initialize the list markers.
    newList = list()
    a = 0
    b = 0

    # Merge the two lists together until one is empty.
    while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            newList.append(listA[a])
            a += 1
        else:
            newList.append(listA[a])
            b += 1
    
    # If listA contains more items, append them to newList.
    while a < len( listA):
        newList.append(listA[a])
        a += 1
    
    # Or if listB contains more items, append them to newList.
    while b < len(listB):
        newList.append(listB[b])
        b += 1
    return newList
    
    














