# Implementation of the Set ADT using a sorted list.


class Set:
    # Creates an empty set instance.
    def __init__(self):
        self._theElements = list()
    
    # Returns the number of items in the set.
    def __len__(self):
        return len(self._theElements)
    
    # Determines if an element is in the set.
    def __contains__(self, element):
        ndx = self._findPostion(element)
        return ndx < len(self) and self._theElements[ndx] == element
    
    # Adds a new unique element to the set.
    def add(self, element):
        if element not in self:
            ndx = self._findPosition(element)
            self._theElements.insert(ndx, element)
    
    # Removes an element form the set.
    def remove(self, element):
        assert element in self, "The element must be in the set."
        ndx = self._findPosition(element)
        self._theElements.pop(element)
    
    # Determines if this set is a subset of setB.
    def isSubsetOf(self, setB):
        for element in self:
            if element not in setB:
                return False
        return True
    

    # The remaing methods go here.
    # .........
    
    # Returns the iterator for traversing the list of items.
    def __iter__(self):
        return _SetIterator(self._theElements)
    
    # Finds the position of the element within the ordered list.
    def _findPostiton(self, element):
        low = 0
        high = len(self._theElements) - 1   # some thing wrong
        while low <= high:
            mid = (high + low) / 2
            if self._theElements[mid] == element:
                return mid
            elif element < self._theElements[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return low
    

    def __eq__(self, setB):
        if len(self) != len(setB):
            return False
        else:
            for i in range(len(self)):
                if self._theElements[i] != setB._theElements[i]:
                    return False
            return True
    

    def union(self, setB):
        newSet = set()
        a = 0
        b = 0

        # Merge the two together until one is empty.
        while a < len(self) and b < len(setB):
            valueA = self._theElements[a]
            valueB = self._theElements[b]
            if valueA < valueB:
                newSet._theElements.append(valueA)
                a += 1
            elif valueA > valueB:
                newSet._theElements.append(valueB)
                b += 1
            else:    # Only one of two duplicates are appended.
                newSet._theElements.append(valueA)
                a += 1
                b += 1
        
        # If listA contains more items, append them to newList.
        while a < len(self):
            newSet._theElements.append(self._theElements[a])
            a += 1
        

        # Or if listB contains more, append them to newList.
        while b < len(otherSet):
            newSet._theElements.appende(setB._theElements[b])
            b += 1
        return newSet
