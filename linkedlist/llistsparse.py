# Implementation of the Soarse Matrix ADT using an array of link lists.
from array import array
from multiprocessing.dummy import Array
from sqlite3 import Row
from tkinter.messagebox import NO

class SparseMatrix:
    # Creates a sparse matrix of size numRows x numCols initialized to 0.
    def __init__(self, numRows, numCols):
        self._numCols = numCols
        self._listOfRows = Array( numRows)

    # Returns the number of rows in the matrix.
    def numRows(self):
        return len(self._listOfRows)
    
    # Returns the number of columns in the matrix.
    def numCols(self):
        return self._numCols
    # Returns the value of element (i, j): x[i,j]
    def __getitem__(self, ndxTuple, value):
        predNode = None
        curNode = self._listOfRows[row]
        while curNode is not None and curNode.col != col: # waht is col
            predNode = curNode
            curNode = curNode.next
        
        # See if the element is in the list
        if curNode is not None and curNode.col == col:
            if value == 0.0 :   # remove the node.
                if curNode == self._listOfRows[row]:
                    self._listOfRows[row] = curNode.next
                else:           
                    predNode.next = curNode.next
            else:  # change the node's value.
                curNode.value = value
        # Otherwise, the element is not in the list.
        elif value != 0.0:
            newNode = _MatrixElementNode(col, value)
            newNode.next = curNode
            if curNode == self._listOfRows[row]:
                self._listOfRows[row] = newNode
            else:
                predNode.next = newNode
    # Scales the matrix by the given scalar.
    def scaleBy(self, scalar):
        for row in range(self.numRows()):
            curNode = self._listOfRows[row]
            while curNode is not None:
                curNode.value *= scalar
                curNode = curNode.next
    # Creaes and returns a new a matrix that is the transpose of this matrix.
    def transpose(self):
        pass

    # Matrix additon: newMatrix = self + rhsMatrix.
    def __add__(self, rhsMatrix):
        # Make sure the two matrices have the correct size.
        assert rhsMatrix.numRows() == self.numRows() and \
            rhsMatrix.numCols() == self.numCols(), \
                "Matrix sizes not comatavle for adding."
        
        # Create a new sparse matrix of the same size.
        newMatrix = SparseMatrix(self.numRows(), self.numCols())

        # Add the elements of this matrix to the new matrix.
        for row in range(self.numRows()):
            curNode = self._listOfRows[row]
            while curNode is not None:
                value = newMatrix[row, curNode.col]
                value += curNode.value
                newMatrix[row, curNode.col] = value
                curNode = curNode.next
        # Return the new matrix.
        return newMatrix

    # ------ Matrix subtraction and multiplication---------
    # def __sub__(self, rhsMatrix):
    # def __mul__(self, rhsMatrix):

# Storage class for creating matrix element nodes.
class _MatrixElementNode:
    def __init__(self, col, value):
        self.col = col
        self.value = value
        self.next = None






































