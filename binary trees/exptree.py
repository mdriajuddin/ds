from queue import Queue


class ExpressionTree:
    # Builds an expression tree for the expression string.
    def __init__(self, expStr):
        self._expTree = None
        self._buildTree(expStr)
    
    # Evaluates th eexpreession tree and returns th eresulting value.
    def evaluate(self, varMap):
        return self._evalTree(self._expTree, varMap)
    
    # Returns a string representation of the expression tree.
    def __str__(self):
        return self._buildString(self._expTree)
    

    # Recursively builds a string representation of th expreesion tree.
    def _buildString(self, treeNode):
        # if the node is a leadt, it's an operand.
        if treeNode.left is None and treeNode.right is None:
            return str(treeNode.element)
        else:   # Otherwise, it's an opeator.
            expStr = '('
            expStr += self._buildString(treeNode.left)
            expStr +=  str(treeNode.element)
            expStr += self._buildString(treeNode.right)
            expStr += ")"
            return expStr
    

    def _evalTree(self, subtree, varDict):
        # See if the node is a leaf node, in which case return its value.
        if subtree.left is None and subtree.right is None:
            # Is the operand a literal digit?
            if subtree.element >= "0" and subtree.element <= "9":
                return int(subtree.element)
            else:    # Or is it a variable?
                assert subtree.element in varDict, "Invalid variable."
                return varDict[subtree.element]
        
        # Otherwise, it's an opeator that needs to be computed.
        else:
            # Evaluate the expression in the left and right subtrees.
            lvalue = self._evalTree(subtree.left, varDict)
            rvalue = self._evalTree(subtree.right , varDict)

            # Evaluate the operation using  a helper method.
            return self._computeOp(lvalue, subtree.element, rvalue)
        
    # Compute the arithmentic operation based on the supplied op string.
    def _computeOp(left, op, right):
        pass


    
    def _buildTree(self, expStr):
        # Build a queue containing the tokens in the expreession string.
        expQ = Queue()
        for token in expStr:
            expQ.enqueue(token)
        
        # Create an empty root node.
        self._expTree  = _ExpTreeNode(None)
        # Call the recursive function to build the expression tree.
        self._recBuildTree(self._expTree, expQ)
    
    # Recursively builds the tree given an initial root node.
    def _recBuildTree(self, curNode, expQ):
        # Extract the next token form the queue.
        token = expQ.dequeue()

        # See if the token is a left paren: "("
        if token == "(":
            curNode.left = _ExpTreeNode(None)
            buildTreeRec(curNode.left, expQ)
            
            # The next token will be a ), remove it.
            expQ.dequeue()
        
        # Otherwise, the token is a digit that has to be converted to an int.
        else:
            curNode.element = token









# Storage class for creating the tree nodes.
class _ExpTreeNode:
    def __init__(self, data):
        self.element = data
        self.left = None
        self.right = None


