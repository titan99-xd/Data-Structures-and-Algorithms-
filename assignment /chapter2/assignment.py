1.
#  def insert(self, index: int, val: int) -> None:
#         """
#         Insert a value at the specified index.
#         Creates a new array with increased size and copies elements.
#         """
#         if not isinstance(val, int) or not self._min_val <= val <= self._max_val:
#             raise TypeError(f'Value must be an integer between {self._min_val} and {self._max_val}')

#         if not isinstance(index, int) or index < 0 or index > self._size:
#             raise IndexError('Index out of bounds!')

#         # Save old values before modifying size
#         old_values = [self.__getitem__(i) for i in range(self._size)]

#         # Increase size
#         self._size += 1

#         # Creating a new reserved memory
#         new_resmem = ReservedMemory(self._size * self._bytes_per_element)

#         # Updated memory reference
#         self._resmem = new_resmem

#         # Copy old values back to new memory
#         for i in range(index):
#             self.__setitem__(i, old_values[i])

#         for i in range(index, self._size - 1):
#             self.__setitem__(i + 1, old_values[i])

#         # Insert the new value at the insertion point
#         self.__setitem__(index, val)

2.
# def remove(self, index: int) -> int:
#         """
#         Remove an element at the specified index.
#         Returns the value of the removed element.
#         Raises IndexError if index is out of bounds.
#         Returns None if the array is empty.
#         """
#         # Check if array is empty
#         if self._size == 0:
#             return None

#         # Check if index is valid
#         if not isinstance(index, int) or index < 0 or index >= self._size:
#             raise IndexError('Index out of bounds!')

#         # Get the value to return
#         removed_value = self.__getitem__(index)

#         # Save all old values before we modify size
#         old_values = [self.__getitem__(i) for i in range(self._size)]

#         # Decrease size
#         self._size -= 1

#         # Create new reserved memory (smaller)
#         if self._size > 0:
#             new_resmem = ReservedMemory(self._size * self._bytes_per_element)

#             # Update memory reference
#             self._resmem = new_resmem

#             # Copy values back, skipping the removed element
#             new_index = 0
#             for i in range(len(old_values)):
#                 if i != index:
#                     self.__setitem__(new_index, old_values[i])
#                     new_index += 1
#         else:
#             # If size becomes 0, no memory needed
#             self._resmem = None

#         return removed_value

3.
#  def search(self, val: int) -> int:
#         """
#         Search for a value in the array.
#         Returns the first index where the value is found, or -1 if
#         not found.
#         """

#         for i in range(self._size):
#             if self.__getitem__(i) == val:
#                 return i
#         return -1
