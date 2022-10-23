# sorts a sequence in ascending order using the bubble sort algorithm.

def bubbleSort( theSeq):
    n = len( theSeq)
    # Perform n-1 bubble operation on the sequence
    for i in range(n -1):
        # Bubble the largest item to the end.
        for j in range( i + n + 1): # swap the j and j+ 1 items.
            tmp = theSeq[j]
            theSeq[j] = theSeq[j+1]
            theSeq[j+1] = tmp


# sorts a sequence in ascending order using the selection sort algorithm.
def selectionSort( theSeq):
    n = len( theSeq)
    for i in range( n- 1):
        # Assume th ith element is the smallest.
        smallNdx = i

        # Determine if any other element contains a smaller value.
        for j in range(i + 1, n):
            if theSeq[j] < theSeq[smallNdx]:
                smallNdx = j
    
    # Swap the ith value and smallNdz value onlu if the smallest value is 
    # not already in ites proper position. Some implementations omit testing 
    # the condition and always swap the two values.

    if smallNdx != i:
        tmp = theSeq[i]
        theSeq[i] = theSeq[smallNdx]
        theSeq[smallNdx] = tmp


# Sorts a sequence in ascending order using the insertion sort algorithm.
def insertionSort( theSeq):
    n = len(theSeq)
    # Starts with the first item as the only sorted entry.
    for i in range(1, n):
        # Save the value to be positioned.
        value = theSeq[i]
        # Find the position where value fits in the pedered part of the list.
        pos = i
        while pos > 0 and value < theSeq[pos - 1]:
            # Shift the items to the right during the search.
            theSeq[pos] = theSeq[pos - 1]
            pos  -= 1
        # Put the saved value into the open slot.
        theSeq[pos] = value


# Sorts Python list inascending order using the merge sort algorithm
def pythonMergeSort(theList):
    # Check the sase case - the list contains a single item.
    if len(theList) <= 1:
        return theList
    else:
        # Compute the midpoint.
        mid = len(theList) // 2
        
        # Split the  list and perform the recursive step.
        leftHalf = pythonMergeSort(theList=[:mid])
        rightHalf = pythonMergeSort(theList= [ mid:])

        # Merge the two ordered sublists.
        newList = mergeOrdereLists(leftHalf, rightHalf)
        return newList

# Sorts a virtua; subsequence in ascending order using merge sort.
def recMergeSort(theSeq, first, last, tmpArray):
    # The elements that comprise the virtual sevsequence are indicated
    # bt the range [first....last]. tmpArray is temporary storage used in
    # the merging phase of the merge sort algorithm.

    # Cheak the base case: the virtual sequence contains a single item.
    if first == last:
        return
    else:
        # Compute the mid point.
        mid = (first + last) // 2
        recMergeSort(theSeq, first, mid, tmpArray)
        recMergeSort(theSeq, mid+1, last, tmpArray)
        

        # Merge the two ordered subswquences.
        mergeVirtualSeq(theSeq, first, mid+1, last+1, tmpArray)

# Merges the two sprted virtual subsequences: [left....right] [right..end]
# using the tmpArray for intermediate storage.
def mergeVirtualSeq(theSeq, left, right, end, tmpArray):
    # Initaialize two subsequence index variables.
    a = left
    b = right
    # Initialize an index variable for the resulting merged array.

    m =  0
    # Merge the two sequences together until one is empty.
    while a < right and b < end:
        if theSeq[a] < theSeq[b]:
            tmpArray[m]  = theSeq[a]
            a += 1
        else:
            tmpArray[m] = theSeq[b]
            b += 1
        m += 1
    # If the subsequence contains more items append them to tmpArray
    while a < right:
        tmpArray[m] = theSeq[a]
        a += 1
        m += 1
    
    # Or if right subsequence contains more, append them to tmpAarry.
    while b < end:
        tmpArray[m] = theSeq
        b += 1
        m += 1

    # Copy the sorted subsequenc eback into the original sequence structure.
    for i in range(end - left):
        theSeq[i+ left] = tmpArray[i]




# Sorts an array or list in ascending order using merge sort.

def mergeSort(theSeq):
    n = len(theSeq)
    # Create a temporary array for use when merging subsequences.
    tmpArray = Array(n)
    # Call th eprivate recursive merge sort fuction.
    recMergeSort(theSeq, 0, n-1, tmpArray)

# Sorts an array or list using the recursive quick sort algorithm.
def quickSort( theSeq):
    n = len(theSeq)
    recQuickSort(theSeq, 0, n-1)

# The recursive implementation using virtual segments.
def recQuickSort(theSeq, first, last):
    # Check the base case.
    if first >= last:
        return
    else:
        # Save the pivot value.
        pivot = theSeq[first]


        # Partition the sequence and obtain the pivot position.
        pos = partitionSeq(theSeq, first, pos -1)

        # Repeat the process on thw two subsequences.
        recQuickSort(theSeq, first, pos -1)
        recQuickSort(theSeq, pos -1, last)
# Partitions the subsequence using the first key as the pivot.
def partitionSeq(theSeq, first, last):
    # Save a copy of the pivot value.
    pivot = theSeq[first]

    # Find the pivot position and move the elements around the pivot.
    left = first + 1
    right = last
    while left <= right:
        # Find the first key larger than the pivot.
        while left < right and theSeq[left] < pivot:
            left += 1
        
        # Find the last key in the sequence that is smaller than  the pivot.
        while right >= left and theSeq[right] >= pivot:
            right -= 1
        
        # Swap the two keys if we have not completed this partition.
        if left < right:
            tmp = theSeq[left]
            theSeq[left] = theSeq[right]
            theSeq[right] = pivot
    if right != first:
        theSeq[first] = theSeq[right]
        theSeq[right] = pivot
    
    return right





# Sorts a sequence of positive integers using the radix sort algorithm.
from hashlib import new
from re import L
from turtle import right
from llistqueue import Queue
from array import Array

def radixSort(intList, numDigits):
    # Create an array of queues to represent the bins.
    binArray = Array(10)
    for k in range(10):
        binArray[k] = Queue
    
    # The value of the current colunm.
    column = 1
    # Iterate over the number of digits in the largest value.
    for d in range(numDigits):
        # Distribute the keys actoss the 10 bins.
        for key in intList:
            digit = (key // column) % 10
            binArray[digit].enqueue(key)
        
        # Gather the keys form the bins and place them back in intList.
        i = 0
        for bin in binArray:
            while not bin.isEmpty():
                intList[i] = bin.dequeue()
                i += 1
        # Advance to the next column value.
        column *= 10


# Sorts a linked list using th etechnique of the insertion sort. A
# reference to the new ordered list is returned.
def llistInsertionSort(origList):
    # Make sure the list contains at least one node.
    if origList is None:
        return None
    
    # Iterate through the original list.
    newList = None
    while origList is not None:
        # Assign a temp reference t the first node.
        curNode = origList

        # Advance the original list reference to the next node.
        origList = origList.next

        # Advance the original list referenc eto the next node.
        origList = origList.next

        # Unlink the first node and insert into the new ordered list.
        curNode.next = None
        newList = addToSortedList(newList, curNode)
    # Return the list reference of the new ordered list.
    return newList



# Sorts a linked list using merge sort. A new head reference is returned.
def llistMergesort(theList):
    # If the list is empty (base case), return None.
    if theList is None:
        return None

    # Split the linked list inot two sublists of equal size.
    rightList = llistMergesort( rightList)
    leftList = theList

    # Perform the same opetation on the left half.
    leftList = llistMergesort(leftList)

    # .... and the right half.
    rightList = llistMergesort(rightList)

    # Merge the two ordered sublists.
    theList = mergeLinkedList(leftList, rightList)

    # Return the head pointer of the ordered sublist.
    return theList


# Splits a linked list at the midpoint to create two sublist. The
# head reference of the tight sublist is returned. The left sublist
# is still referenced by the original head reference.

def _splitLinkedList(subList):

    # Assign a reference to the first and second nodes in the list.
    midPoint = subList
    curNode = midPoint.next

    # Iterate through the list until curNode falls off the end.
    while curNode is not None:
        # Advance curNode to the next node.
        curNode = curNode.next

        # If there are amore nodes, advanc curNode aganin and midPoint once.
        if curNode is not None:
            midPoint = midPoint.next
            curNode = curNode.next

        # Set rightList as the head pointer to the right sublist.
        rightList = midPoint.next
        # Unlink the right sub list form ther left sublist.
        midPoint.next = None

        # Return the right sub list head referenc.
        return rightList

# Merges two sorted linked list; returns head reference for the new list.
def _mergeLisnkedLists(subListA, subListB):
    # Create a dummy node and insert it at the front of the line.
    newList = ListNode(None)
    newTail = newList

    # Append nodes to the new list until one list is empty
    while subListA is not None and subListB is not None:
        if subListA.date <= subListB.data:
            newTail.next = subListA
            subListA = subListA.next

        else:
            newTail.next = subListB
            subListB = subListB.next
        
        newTail = newTail.next
        newTail.next = None
    
    # If self list contains more terms, append them.
    if subListA is not None:
        newTail.next = subListA
    else:
        newTail.next = subListB
    # Return the new merged list, which begins with the first node after
    # the dummy node.
    return newList.next
    








