# Implementation of the Matrix ADT using a 2-D array.

from array import Array2D

class Matrix:
    # Creates a matrix of size numRows x numCols initialized to 0.
    def __init__(self, numRows, numCols) -> None:
        self._theGrid = Array2D(numRows, numCols)
        self._theGrid.clear(0)

    # Return the number of colums in the matrix.
    def numRows(self):
        return self._theGrid.numRows()
    
    # Returns the number of columns in the matrix.
    def numCols(self):
        return self._theGrid.numCols()
    
    # Returns the value of element (i, j): x[i,j]
    def __getitem__(self, ndxTuple):
        return self._theGrid[ndxTuple[0],ndxTuple[1]]
    

    # Sets the value of element (i, j) to the value s: x[i,j] = s
    def __setitem__(self,ndxTuple, scalar):
        self._theGrid[ndxTuple[0],ndxTuple[1]] = scalar
    
    # Scales the matrix by the given scalar.
    def scaleBy(self, scalar):
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                self[r, c] *= scalar
    

    # Creates and returns a new matrix that results form matrix addition.
    def __add__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and \
            rhsMatrix.numCols() == self.numCols(), \
                "Matrix sizes not compatible for the add operation."
        # Create the new matrix.
        newMatrix = Matrix(self.numRows(), self.numCols())
        # Add the corresponding elements in the two matrices.
        for r in range(self.numRows()):           
            for c in range(self.numCols()):
                newMatrix[r, c] = self[r, c] + rhsMatrix[ r, c]
        return  newMatrix
    
    # Creates and returns new matrix that results form matrix subraction.
    def __sub__(self, rhsMatrix):
        pass
    # Creates and returns a new matrix resulting form matrix multiplication.
    def __mul__(self,rhsMatirx):
        pass
    
        







































































