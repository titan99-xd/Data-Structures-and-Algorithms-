# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# def print_list(head):
#     current = head
#     while current is not None:
#         print(current.data)
#         current = current.next
#     print("End of list")


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

#     def __repr__(self):
#         return self.data


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def __repr__(self):
#         node = self.head
#         nodes = []
#         while node is not None:
#             nodes.append(node.data)
#             node = node.next
#         nodes.append("None")
#         return " -> ".join(nodes)


# a = Node("a")
# b = Node("b")
# c = Node("c")

# llist = LinkedList()
# llist.head = a
# a.next = b
# b.next = c
# print(llist)


# 1.4 list revision
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

#     def __repr__(self):
#         return str(self.data)


# class LinkedList:
#     def __init__(self, nodes=None):
#         self.head = None

#         if nodes is not None:
#             # create head
#             self.head = Node(nodes.pop(0))
#             node = self.head

#             # create rest of the nodes
#             for elem in nodes:
#                 node.next = Node(elem)
#                 node = node.next

#     def __iter__(self):
#         node = self.head
#         while node is not None:
#             yield node
#             node = node.next

#     def __repr__(self):
#         nodes = []
#         for node in self:
#             nodes.append(str(node.data))
#         nodes.append("None")
#         return " -> ".join(nodes)


# # Create a linked list using a list
# llist = LinkedList(["a", "b", "c", "d", "e"])

# # Print the whole list
# print(llist)

# # Traverse and print each node using a for-loop
# for node in llist:
#     print(node.data)


# 1.class, 2.True, 3.They are sequqnces, 4.flow control, 5.!=,>=, 6.True, 7.Correctness, 8.True, 9.Analyze alogrithm performance, 10.0(1)

# 1,2,3,4,5,6,8,9,10 are correct
# 7 is incorrect - it should be "class complexity"
