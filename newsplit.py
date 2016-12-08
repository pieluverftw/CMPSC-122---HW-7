def new_split_iter(expr):
    OPER = "()+-*/%=;:?<>! "
    pos = 0                     # begin at first character position in list
    expr = expr + ';'
    while expr[pos] != ';':     # repeat until end of input found
        # If there is a space, skip it
        if expr[pos] == ' ':
            pass

        elif expr[pos].isdigit():               # Return Digit
            to_yield = expr[pos]
            while expr[pos + 1].isdigit():
                pos += 1
                to_yield += expr[pos]
            yield to_yield

        elif expr[pos].isalpha():               # Return Variable
            to_yield = expr[pos]
            while expr[pos + 1] not in OPER:
                pos += 1
                to_yield += expr[pos]
            yield to_yield

        elif expr[pos] in OPER:                 # Return Operator
            to_yield = expr[pos]
            if expr[pos + 1] == '=':            # For <= and >=
                pos += 2
                to_yield += '='
            yield to_yield
        pos += 1
    yield ';'


if __name__ == "__main__":
    print (list(new_split_iter("3 + 4*25")))
    print (list(new_split_iter("  3+4 * 25  ")))
