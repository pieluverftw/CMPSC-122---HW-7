"""This module implements a singly linked list
This solution is intended for the benefit of the students
taking CMPSC 122 at the Pennsylvania State University
during the Fall Semester of 2016, and is not intended
for any other audience, or to distributed outside of the course.

Roger Christman, Pennsylvania State University
"""

class LinkedList:
    """A simple singly linked list"""
    class Node:
        """A simple singly linked list node"""
        __slots__ = "_value","_next"
        def __init__(self, v, n):
            self._value = v
            self._next = n
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    def push(self,value):
        """Place a value at the front of the list"""
        self._head = LinkedList.Node( value, self._head )
        if self._tail is None:      # empty list
            self._tail = self._head
        self._size += 1 
    def pop(self):
        """Retrieve a value from front of the list
        This implemenation assumes the list is not empty"""
        result = self._head._value
        self._head = self._head._next
        if self._head is None:      # now empty list
            self._tail = None
        self._size -= 1
        return result
    def __iter__(self):
        current = self._head
        while current is not None:
            yield current._value
            current = current._next
    def top(self):
        return self._head._value
    def is_empty(self):
        return self._head is None
    def __len__(self):
        return self._size
    def __str__(self):
        return ' '.join( iter(self) )

if __name__ == "__main__":
    L1 = LinkedList()
    L1.push("3")
    L1.push("2")
    L1.push("X")
    print("Popped", L1.pop())
    print("Top is", L1.top())
    print("Remaining is", list(L1))
    for s in ["1","...","Testing"]:
        L1.push(s)
    print(len(L1),'elements in',L1)
    L2 = LinkedList()
    while not L1.is_empty():
        L2.push(L1.pop())
    print(L2)
        
        
        
