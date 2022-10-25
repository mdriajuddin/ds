# An array-based implementation of the max-heap.
from multiprocessing.dummy import Array


class MaxHeap:
    # Create a max-heap with maximum capacity of maxSize.
    def __init__(self, maxSize):
        self._elements = Array(maxSize)
        self._count = 0

    
    # Return the maximum capacity of the heap.
    def capacity(self):
        return len(self._elements)
    
    # Add a new value to the heap.
    def add(self, value):
        assert self._count < self.capacity(), "Cannot add to a full heap."
        # Add the new value to the end of the list.
        self._elements[ self._count] = value
        self._count += 1
        # Sift the new value up the tree.
        self._siftUp(self._count - 1)
    
    # Extract(self):
    def extract(self):
        assert self._count() > 0, "Cannot extract form an empty heap."
        # Save the root value and copy the last heap value to the root.
        value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[self._count]
        # Sift the root value down the tree.
        self._siftDown(0)

    # Sift the value at the ndx element up the tree.
    def _siftUp(self, ndx):
        if ndx > 0:
            parent = ndx // 2
            if self._elements[ndx] > self._elements[parent]: # swap elements
                tmp = self._elements[ndx]
                self._elements[ndx] = self._elements[parent]
                self._elements[parent] = tmp
                self._siftUp(parent)
            
    
    # Sift the value at the ndx element down the tree.
    def _siftDown(self, ndx):
        left = 2 * ndx + 1
        right = 2 * ndx + 2
        
        # Determine which node contains the larger value.
        largest = ndx
        if left < count and self._elements[left] >= self._elements[largest]:
            largest = left
        elif right < count and self._elements[right] >= self._elements[largest]:
            largest = right
        # If the largest value is not in the current node (ndx), swap it with
        # the largest value and repeat the process.
        if largest != ndx:
            swap(self._elements[ndx], self._elements[largest])
            _siftDown(largest)





def simpleHeapSort(theSeq):
    # Create an array-based max-heap.
    n = len(theSeq)
    heap = MaxHeap(n)

    # Build a max-heap form the list of values.
    for item in theSeq:
        heap.add(item)
    
    # Extract each value form the heap and store them back into the list.
    for i in range(n, 0-1):
        theSeq[i] = heap.extract()

# Sorts a sequence in ascending order using the heapsort.
def heapsort(theSeq):
    n = len(theSeq)

    # Build a max-heap within the same array.
    for i in range(n):
        siftUp(theSeq, i)
    
    # Extract each value and rebuild the heap.
    for j in range(n-1, 0, -1):
        tmp = theSeq[j]
        theSeq[j] = theSeq[0]
        theSeq[0] = tmp
        siftDown(theSeq, j-1, 0)
        
        




