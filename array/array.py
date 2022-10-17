# Implements the Array ADT using array capabilities of the ctypes module.

import ctypes

class Array:
    # Creates an array with size elements.
    def __init__(self, size):
        assert size > 0, "Array size must be > 0"
        self._size = size
        # Create the array structure using the ctypes module.
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        # Initialize each elelment.
        self.clear(None)
    
    # Reutrns the size of the array.
    def __len__(self):
        return self._size
    # Gets the contents of the index elements.
    def __getitem__(self, index):
        assert index >=0 and index < len(self), "Array subscripts out of range"
        return self._elements[ index ]

    # Puts the value in the array element at index position.
    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        self._elements[index]  = value

    # Returns the array's iterator for traversing the elements.
    def __iter__(self):
        return _ArrauIterator(self._elements)


# An iterator for the Array ADT.
class _ArrayIterator:
    def __init__(self, the Array):
        self._arrayRef = theArray
        self._curNdx = 0
    
    def __iter__(self):
        return self
    def __next__(self):
        if self._curNdx < len(self._arrayRef):
            entry = self._arrayRef[ self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration




# Implementation of the Array2D ADT using an array of array.
class Array2D:
    # Creates a 2-D array of size numRows x numCols.
    def __init__(self, numnRows, numCols) -> None:
        # Create a 1-D array to store an array reference for each row.
        self._theRows = Array(numnRows)

        # Create the 1-D array to store row of the t2-D arrary.
        for i in range(numnRows)
        self._theRows[i] = Array(numCols)
    
    # Returns the number of rows in the 2-D array.
    def numRows(self):
        return len(self._theRows)
    
    # Returns the number of colums in the 2-D array.
    def numCols(self):
        return len(self._theRows[0])
    
    # Clears the array by setting every element to the given value.
    def clear(self, value):
        for row in range(self.numRows()):
            row.clear(value)
    

    # Gets the contents of the element at position [i, j]
    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
            and clo >= 0 and clo < self.numCols(), \
                "Array subscript out of range."
        theIdAray = self._theRows[row]
        return theIdAray[col]

    

    # Sets the contents of the element at position [i, j] to value.
    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == 2, "Invalid number of array subsctipts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
            and col >= 0 and col < self.numCols(), \
                "Array subscript out of range."
        theIdArray = self._theRows[row]
        theIdArray[col] = value





