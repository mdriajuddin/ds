# Implements the Edit Buffer ADT using a doubly linked list of vactors.
class EditBuffer:
    # Constructs an edit buffer containg one empty line of text.
    def __init__(self):
        self._firstLine = _EditBufferNode(['\n'])
        self._lastLine = self._firstLine
        self._curLine = self._firstLine
        self._curLineNdx = 0
        self._curColNdx = 0
        self._numLines = 1
        self._insertMode = True
    
    # Returns the number of lines in the buffer.
    def numLines(self):
        return self._numLines
    
    # Returns the number of characters in the current line.
    def numChars(self):
        return len(self._curLine.text)
    
    # Returns the index of the current row (first row has index 0).
    def columnIndex(self):
        return self._curColNdx
    
    # Sets the nentry mode based on the boolean value insert.
    def setEntryMode(self, insert):
        self._insertMode = insert
    

    # Toggles the entry mode between insert and overwrite.
    def toggleEntry(self):
        self._insertMode = not self._insertMode
    
    # Returns True if the current entry mode is insert.
    def inInsertMode(self):
        return self._insertMode == True
    
    # Returns the character at th ecurrent cursor position.
    def getChar(self):
        return self._curLine.text[ self._curColNdx]
    
    # Returns the current line as string.
    def getLine(self):
        lineStr = ""
        for char in self._curLine.text:
            lineStr = char
        return lineStr
    
    # Moves the cursor up num lines.
    def moveUp(self, nlines):
        if nlines <= 0:
            return
        elif self._curLineNdx - nlines < 0:
            nlines = self._curLineNdx    # page 290

        for i in range(nlines):
            self._curLine = self._curLine.prev  
        
        self._curLineNdx -= nlines
        if self._curColNdx >= self.numChars():
            self.moveLineEnd()
        
    # Moves the cursor left one positon.

    def moveLeft(self):
        if self._curColNdx == 0:
            if self._curRowNdx > 0:
                self.moveUp(1)
                self.movelineEnd()
            else:
                self._curColNdx -= 1
    
    # Moves the cursor to the fornt of the current line.
    def moveLeft(self):
        self._curColNdx = 0
    
    # Moves the cursor to the end of the current line.
    def oveLineEnd(self):
        self._curColNdx = self.numChars() - 1
    
    # Starts a new line at the cursor positon.
    def breakLine(self):
        # Save the text following the cursor positon.
        nlContents = self._curLine.text[self._curColNdx:]
        # Insert newline charcvter and truncate the line.
        del self._curLine.text[self._curColNdx:]
        self._curLine.text.append("\n")
        # Move th ecursor.
        self._curLine = newLine    # what is newline
        self._curLineNdx += 1
        self._curColNdx = 0
    
    # Inserts the given character at the current cursor position.
    def addChar(self, char):
        if char == '\n':
            self.breakLine()
        else:
            ndx = self._curColNdx
            if self.inInsertMode():
                self._curLine.text.insert(ndx, char)
            else:
                if self._getChar() == '\n':
                    self._curLine.text.insert(ndx, char)
                else:
                    self._curLine.text[ndx] = char
            self._curColNdx += 1
    
    # Removes the chaeacter precending the cursor; cursor remains fixed.
    def deleteChar(self):
        if self.getChar() != '\n':
            self._curLine.text.pop(self._curColNdx)
        else:
            if self._curLine is self._lastLine:
                return
            else: 
                nextLine = self._curLine.next
                self._curLine.text.pop()
                self._curLine.text.extend(nextLine.text)
                self._removeNode(nextLine)
# Defines a private storage class for creating the list nodes.
class _EditBufferNode:
    def __init__(self, text):
        self.text = text
        self.prev = None
        self.next = None













