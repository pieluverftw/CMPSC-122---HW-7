class BinaryTree:
    class Node:
        __slots__ = "_value", "_left", "_right", "_var"
        def __init__(self, l, vr, v, r, i):
            self._left = l
            self._var = vr
            self._value = v
            self._right = r
            self._index = i
    __slots__ = "_root", "_size"

    # Initialize binary tree with a root value of None
    def __init__(self):
        self._root = None
        self._size = 0
        self._indexAll = 0


    def _search(self, here, var):

        if here is None:
            print(var + " Does not exist")
            return None
        elif var > here._var:
            return self._search(here._right, var)
        elif var < here._var:
            return self._search(here._left, var)
        else:
            print("Found {} with value {}".format(var, here._value))
            return here


    def _insert(self, here, var, value):

        if here is None:
            self._size += 1
            print("Size is now {} and variable {} with value {} has been inserted.".format(self._size, var, value))
            return self.Node(None, var, value, None)

        elif var == here._var:
            print("Found var with value {}. Updating to new value {}".format(here._value, value))
            indexTemp = here._index
            return self.Node(here._left, here._var, value, here._right, indexTemp)

        elif var > here._var:
            self._indexAll += 1
            return self.Node(here._left, here._var, here._value, self._insert(here._right, var, value), self._indexAll)

        elif var < here._var:
            self._indexAll += 1
            return self.Node(self._insert(here._left, var, value), here._var, here._value, here._right, self._indexAll)


    def assign(self, var, value):

        self._root = self._insert(self._root, var, value)

    def _lookup(self, var):

        search_node = self._search(self._root, var)
        if search_node is None:
            print("Variable {} DNE, it is now equal to zero".format(var))
            self.assign(var, 0)
            search_node = self._search(self._root, var)
        return search_node._value

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size


    def searchIndex(self, here, var):
        if here is None:
            print(var + " Does not exist")
            return None
        elif var > here._var:
            return self._search(here._right, var)
        elif var < here._var:
            return self._search(here._left, var)
        else:
            print("Found {} with index {}".format(var, here._value))
            return here._index



if __name__ == "__main__":
    # TEST BINARY TREE IMPLEMENTATION
    """"""
    a = BinaryTree()
    print("Empty: ")
    print(a.is_empty())
    print("Undeclared variable x:")
    x = "x"
    print(str(a._search(a._root, x)))
    print('-' * 50)
    print("Let x = 5")
    a.assign(x, 5)
    print('-' * 50)

    print("Lookup \'x\'")
    a.lookup(x)
    print('-' * 50)

    print("Lookup a value that does not exist (y):")
    y = "y"
    a.lookup(y)
    print('-' * 50)

    print("The bst is empty?")
    print(a.is_empty())
    print('-' * 50)

    print("Test size function:")
    print("Num nodes: ", len(a))
    print('-' * 50)

#    print("Test printing of BST:")
#    print(a)
#    print('-' * 50)
