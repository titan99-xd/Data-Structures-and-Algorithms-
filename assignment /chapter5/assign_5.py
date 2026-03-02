# Question 1:
'''
def _find(self, data):
        """
        Find the node containing the data.

        Parameters:
        - 'data': The data to be found

        Returns:
        - The node that contains such data or None if data is not found
        """
        current_node = self._root_node
        
        while current_node:
            if data == current_node.data:
                return current_node
            elif data < current_node.data:
                current_node = current_node._left_child
            else:
                current_node = current_node._right_child
        
        return None
'''

# Question 2:
'''
def _find(self, data):
        """
        Find the node containing the data.

        Parameters:
        - 'data': The data to be found

        Returns:
        - The node that contains such data or None if data is not found
        """
        current = self._root_node
        while current:
            if current.data == data:
                return current
            elif current.data > data:
                current = current._left_child
            else:
                current = current._right_child
        return None        

    def find_minimum(self):
        """
        Returns the minimum value of the tree
        """
        if self._root_node is None:
            return None
            
        current = self._root_node
        while current._left_child is not None:
            current = current._left_child
        
        return current

    def find_maximum(self):
        """
        Returns the maximum value of the tree
        """
        if self._root_node is None:
            return None
        
        current = self._root_node
        while current._right_child is not None:
            current = current._right_child
        
        return current 
        
'''

# Question 3
'''
 def _find(self, data):
        """
        Find the node containing the data.

        Parameters:
        - 'data': The data to be found

        Returns:
        - The node that contains such data or None if data is not found
        """
        current = self._root_node
        while current:
            if current.data == data:
                return current
            elif current.data > data:
                current = current._left_child
            else:
                current = current._right_child
        return None        

    def _detach_node(self, node):
        """
        Detach a node from the tree. Node to be detached has one child at most.
        An error will be raised otherwise.
        """
        if node is None:
            return
        
        if node._left_child and node._right_child:
            raise ValueError("Cannot detach node with two children")
        
        child = node._left_child if node._left_child else node._right_child
        
        if node._parent is None:
            self._root_node = child
            if child:
                child._parent = NOne
        else:
            parent = node._parent
            
            if parent._left_child == node:
                parent._left_child = child
            else:
                parent._right_child = child
            if child:
                child._parent = parent
                
        node._parent = None
        node._left_child = None
        node._right_child = None
        '''
