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
    