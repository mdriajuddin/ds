# Implementation of the Set ADT container using a Python list.

class Set:
    # Creates an empty set instance.
    def __init(self):
        self._theElements = list()
    
    # Returns the number of items in the set.
    def __len__(self):
        return len( self._theElements)
    
    # Determines if an elements is in the set.
    def __contains__(self, element):
        return element in self._theElements
    
    # Adds a new unique element to the set.
    def add(self, element):
        if element not in self:
            self._theElements.append(element)
    

    # Removes an element form the set.
    def remove(self, element):
        assert element in self, "The element must be in the set."
        self._theElements.remove(element)
    
    # Determines if two sets are equal.
    def __eq__(self, setB):
        if len(self) != len(setB):
            return False
        else:
            return self.isSubsetOF(setB)

    # Determines if this set is a subset of setB.
    def isSubsetOF(self, setB):
        for element in self:
            if element not in setB:
                return False
        return True
    
    # Creates a new set form the union of this set and setB.
    def union(self, setB):
        newSet = Set()
        newSet._theElements.extend(self._theElements)
        for element in setB:
            if element not in self:
                newSet._theElements.append(element)
        return newSet
    
    # Creates a new set form the difference: self set and setB.
    def diffetence(self, setB):
        pass
    # Returns an iterator for traversing the list of items.
    def __iter__(self):
        return _SetIterator(self._theElements)