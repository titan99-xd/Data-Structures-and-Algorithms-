class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList():
    def __init__(self, head=None, tail=None, size=None):
        self._head = head
        self._tail = tail
        self._size - size

    def __iter__(self):
        self._iter_index = self._head
        return self

    def __len__(self):
        return self._size

    def __next__(self):
        if self._iter_index:
            val = self._iter_index.data
            self._iter_index = self._iter_index.next
            return val
        else:
            raise StopIteration

    def __getitem__(self, index):
        if index < 0 or index >= self._size:
            raise (ValueError('Index out of bounds'))
        current_node = self._head
        for _ in range(index):
            current_node = current_node.next
        return current_node.data

    def __setitem__(self, index, val):
        if index < 0 or index >= self._size:
            raise (ValueError('Index out of bounds'))
        current_node = self._head
        for _ in range(index):
            current_node = current_node.next
        current_node.data = val

    def __repr__(self):
        current_node = self._head
        values = ""
        while current_node:
            values += f",{current_node.data}"
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<SinglyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def insert_left(self, val):
        """
        This method is used to append the given value at the begening of the list node        
        """
        new_node = ListNode(val)
        if self._size == 0:
            new_node.next = None
            self._head = self._tail = new_node
        else:
            old_head = self._head
            self._head = new_node
            new_node.next = old_head
            self._tail = self._tail
        self._size += 1

    def insert_End(self, val):
        '''
        This method is used to append the given value at the end of the list node
        '''
        new_node = ListNode(val)
        if self._size == 0:
            new_node.next = None
            self._head = self._tail = new_node
        else:
            old_tail = self._tail
            old_tail.next = new_node
            self._tail = new_node
            new_node.next = None
        self._size += 1

    def insert_Before_Node(self, index, val):
        '''
        This method is use to insert the given value ahead of the given index value 
        '''
        new_node = ListNode(val)
        # first case handle when size = 0
        if self._size == 0:
            new_node.next = None
            self._head = self._tail = new_node
            self._size += 1
            return

        if index < 0 or index >= self._size:
            raise Exception("Index out of bound")

        previous_node = None
        current_node = self._head
        # second case when the size of the list is 1 i,e its head == tail
        if self._head == self._tail:
            self._tail = self._head
            self._tail.next = None
            self._head = new_node
            self._head.next = self._tail

        # third case when we have to insert between two node
        else:
            for _ in range(index):
                previous_node = current_node
                current_node = current_node.next

            # fourth case inserting when list is not unit and have to insert at head
            if current_node == self._head:
                new_node.next = self._head
                self._head = new_node

            # for other default cases
            else:
                previous_node.next = new_node
                new_node.next = current_node
        self._size += 1

    def insert_After_Node(self, index, val):
        '''
        This method is use to insert the given value at the end of the the given index vlaue
        '''
        new_node = ListNode(val)

        # when size is 0
        if self._size == 0:
            self._head = self._tail = new_node
            new_node.next = None
            self._size += 1
            return

        # when index is out of bound
        if index < 0 or index >= self._size:
            raise Exception("Index out of bound")

        current_node = self._head
        next_node = None

        # when size of the listNode is 1
        if self._head == self._tail:
            self._head.next = new_node
            self._tail = new_node
            new_node.next = None
        else:
            for _ in range(index):
                current_node = current_node.next
                next_node = current_node.next
            # if current node is tail
            if current_node == self._tail:
                old_tail = self._tail
                old_tail.next = new_node
                self._tail = new_node
                new_node.next = None
            else:
                current_node.next = new_node
                new_node.next = next_node
        self._size += 1
