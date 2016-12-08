""" A module for an Expression Tree with Class Inheritance

This solution is intended for the benefit of the students
taking CMPSC 122 at the Pennsylvania State University
during the Fall Semester of 2016, and is not intended
for any other audience, or to distributed outside of the course.

Roger Christman, Pennsylvania State University
"""
from abc import ABCMeta,abstractmethod
from vartree import BinaryTree
from machine import

class ExprTree(metaclass=ABCMeta):
    """Abstract class for expression"""
    def __str__(self):
        return ' '.join( str(x) for x in iter(self) )

    #   All of the derived class mus implement these functions
    @abstractmethod
    def __iter__(self):
        """an inorder iterator for this tree node, for display"""
        pass
    @abstractmethod
    def postfix(self):
        """a post-order iterator to create a postfix expression"""
        pass
    @abstractmethod
    def evaluate(self, variables, functions):
        """evaluate using the existing variables"""
        pass


class Value(ExprTree):
    """A Value leaf"""
    def __init__(self, v):
        self._value = v
    def __iter__(self):
        yield self._value
    def postfix(self):
        yield self._value
    def evaluate(self, variables, functions):
        return self._value
    def comp(self):
        newInstr = Instruction(self._value)
        prog.append(newInstr )

class Var(ExprTree):
    """A variable leaf"""
    def __init__(self, n):
        self._name = n
    def __iter__(self):
        yield self._name
    def postfix(self):
        yield self._name
    def evaluate(self, variables, functions):
        return variables.lookup(self._name)
    def comp(self):
        #test
        newInstr = Instruction(variables.lookup(self._name))
        prog.append(newInstr)
        #test end
        #return "T" + variables.searchIndex()

class Oper(ExprTree):
    """A binary operation"""
    def __init__(self, l, o, r, t):
        self._left = l
        self._oper = o
        self._right = r
        self._temp = t
    def __iter__(self):
        yield '('
        yield from self._left
        yield self._oper
        yield from self._right
        yield ')'
    def postfix(self):
        yield from self._left.postfix()
        yield from self._right.postfix()
        yield self._oper
    def evaluate(self, variables, functions):
        if self._oper == '=':
            value = self._right.evaluate(variables, functions)
            variables.assign( self._left._name, value)
            return value
        else:
            v1 = self._left.evaluate(variables, functions)
            v2 = self._right.evaluate(variables, functions)
            return eval( str(v1)+self._oper+str(v2) )
    def comp(self, expr, vartree, functree, resultset):


class Cond(ExprTree):
    """A conditional expression"""
    def __init__(self, b, t, f):
        self._test = b
        self._true = t
        self._false = f
    def __iter__(self):
        yield '('
        yield from self._test
        yield '?'
        yield from self._true
        yield ':'
        yield from self._false
        yield ')'
    def postfix(self):
        pass     # postfix conditional not required
    def evaluate(self, variables, functions):
        if self._test.evaluate(variables, functions):
            return self._true.evaluate(variables, functions)
        else:
            return self._false.evaluate(variables, functions)

class Func(ExprTree):
    def __init__(self, n, p):
        self._name = n
        self._par = p
    def __iter__(self):
        yield "("
        yield self._name
        yield "("
        yield self._par
        yield ")"
        yield ")"
    def postfix(self):
        pass
    def evaluate(self, variables, functions):
        func_para, expr = functions.lookup(self._name)
        temp = BinaryTree()
        for i in range(0, len(func_para)):
            temp.assign(func_para[i], self._par[i].evaluate(variables, functions))
        return expr.evaluate(temp, functions)
    def comp(self):
        pass

class compile_tree(ExprTree):
    def __init__ (self, op):

class Print(ExprTree):



if __name__ == '__main__':
    V = BinaryTree()
    F = BinaryTree()
    VA = Var("A")
    Sum = Oper(Value(2),'+',Value(3))
    A = Oper(VA,'=',Sum)
    print( "Infix iteration: ", list(A) )
    print( "String version ", A )
    print( "Postfix iteration: ", list(A.postfix() ))
    print( "Execution: ", A.evaluate(V, F) )
    print( "Afterwards, A = ", VA.evaluate(V, F) )

    # If A == 5, return A+2 else return 3
    CondTest = Cond(Oper(VA,'==',Value(5)),Oper(VA,'+',Value(2)),Value(3))
    print( CondTest,'-->',CondTest.evaluate(V, F) )
    
        
