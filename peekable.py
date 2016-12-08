class Peekable():

    def __init__(self, iterator):

        self._iterator = iterator
        self._peeked = None

    def __iter__(self):
        return self

    def __next__(self):

        if self._peeked is None:
            self._peeked = next(self._iterator)
        ans = self._peeked
        self._peeked = None     # we don't yet see what comes next
        return ans

    def peek(self):

        if self._peeked is None:
            self._peeked = next(self._iterator)
        return self._peeked



def peek(x):
    return x.peek()


if __name__ == "__main__":
    i = Peekable(iter([1, 2, 3, 4, 5]))
    print(peek(i))        # peek at the 1
    print(peek(i))        # and again
    print(next(i))        # should also be the 1 we were looking at
    print(next(i))        # move on and return 2
    print(next(i))        # move on and return 3
    print(peek(i))        # peek at the 4
    print(next(i))        # which is still there before this advances
    print(list(Peekable(iter([1, 2, 3, 4, 5]))))   # still iterates normally
