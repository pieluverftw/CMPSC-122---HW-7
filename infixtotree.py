""" A parser for infix expressions that produces an expression tree

This solution is intended for the benefit of the students
taking CMPSC 122 at the Pennsylvania State University
during the Fall Semester of 2016, and is not intended
for any other audience, or to distributed outside of the course.

Roger Christman, Pennsylvania State University
"""

from peekable import Peekable, peek
from newsplit import new_split_iter
from exprtree import Value,Var,Oper,Cond,Func

def tree_assign( iter ):
    left = tree_cond( iter )
    if peek(iter) == '=':
        next(iter)
        right = tree_assign( iter )
        return Oper( left, '=', right )
    else:
        return left

def tree_cond( iter ):
    left = tree_rel( iter )
    if peek(iter) == '?':
        next(iter)
        true_case = tree_cond( iter )
        next(iter)  # : expected
        false_case = tree_cond( iter )
        return Cond( left, true_case, false_case )
    else:
        return left

def tree_rel( iter ):
    left = tree_sum( iter )
    oper = peek(iter)
    while oper in ['<','<=','>','>=','!=','==']:
        next(iter)
        right = tree_sum( iter )
        left = Oper( left, oper, right )
        oper = peek(iter)
    return left

def tree_sum( iter ):
    left = tree_product( iter )
    oper = peek(iter)
    while oper == '+' or oper == '-':
        next(iter)
        right = tree_product( iter )
        left = Oper( left, oper, right )
        oper = peek(iter)
    return left

def tree_product( iter ):
    left = tree_factor( iter )
    oper = peek(iter)
    while oper == '*' or oper == '/' or oper == '%':
        next(iter)
        right = tree_factor( iter )
        left = Oper( left, oper, right )
        oper = peek(iter)
    return left

def tree_factor( iter ):
    item = next(iter)
    if item == '(':
        res = tree_assign( iter )
        next(iter)
        return res
    elif item.isdigit():
        return Value(item)
    elif peek(iter) == '(':
        args = []
        while peek(iter) != ')':
            next(iter)
            temp = tree_assign(iter)
            args.append(temp)
        next(iter)
        return Func(item, args)
    else:
        return Var(item)
"""
    elif item.isalpha():
        if next(iter) == "(":
            par = []
            par.append(next(iter))
            next(iter)
            while peek(iter) is not ")":
                next(iter)
                temp = tree_assign(iter)
                par.append(temp)
            next(iter)
            return Func(item, par)      # Passes token of name and parameter
"""

    
def to_expr_tree( expr ):
    return tree_assign(Peekable((new_split_iter(expr))))


def iter_to_tree(iterator):
    return tree_assign(iterator)

def define_func(iterator):
    next(iterator)              # "deffn"
    name = next(iterator)       # function name
    next(iterator)              # (
    parms = [next(iterator)]    # first argument
    while next(iterator)==',':
        parms.append(next(iterator))
    next(iterator)              # =
    return name, parms, tree_assign(iterator)

if __name__ == "__main__":
    print (to_expr_tree("5"))
    print (to_expr_tree("A = 5"))
    print (to_expr_tree("A = 2 + 3 * B - xyz"))
    print (to_expr_tree("x < 0 ? 0 - x : x"))
