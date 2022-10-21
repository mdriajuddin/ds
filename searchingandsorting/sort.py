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






