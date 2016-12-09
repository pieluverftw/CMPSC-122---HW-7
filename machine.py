class Instruction:
    """Simple instructions representative of a RISC machine

    These instructions are mostly immutable -- once constructed,
    they will not be changed -- only displayed and executed
    """
    def __init__(self, t):      # default constructor
        self._temp = t          # every instruction has a register
    def get_temp(self):         #     which holds its answer
        return self._temp

class Print(Instruction):
    """A simple non-RISC output function to display a value"""
    def __str__(self):
        return "print T" + str(self._temp)
    def execute(self,temps,stack,pc,sp):
        print( temps[self._temp] )

class Init (Instruction):
    # test
    def __init__(self, v):
        self._value = v
    def __str__(self):
        return "T" + str(self._temp) + " = " + str(self._value)
    #Instruction._temp += 1
    def execute(self, temps, stack, pc, sp):
        return temps[self._temp]
    # /test

class Load (Instruction):
    def __init__(self, var, variables, pc, sp):
        self._temp = variables.lookup(var)
        self._stackPoint = sp
        self._progCode = pc

    def __str__(self, variables):
        return  "T" + str(self._temp) + " = stack[" + str(self._stackPoint) + "]"

    def execute(self, temps, stack, pc, sp):
        temps[self._temp] = stack[sp]
        return temps[self._temp]

    # test
    # temp[t]= v1
    # Instruction._temp += 1
    # /test

class Store(Instruction):
    def __init__(self, instr, var, variables):
        self._var = var
        self._tree = variables
        variables.assign(var, instr.compute())          # instr not yet defined
        self._stackPoint = variables.lookup(var)

    def __str__(self, variables):
        return "stack[" + str(self._stackPoint) + "] = T" + str(self._temp)

    def execute(self, temps, stack, pc, sp):
        stack[sp] = temps[self._temp]
        # return stack[sp]                              # If the function wants to return the exact value
        return self._tree.lookup(self._var)

    # test
    #stack.push(temp[t]0)
    #Instruction._temp += 1
    #return
    # /test

class Compute(Instruction):
    def __init__ (self, l, op, r):
        self._left = l
        self._oper = op
        self._right = r

    def __str__ (self):
        return "T" + str(self._temp) + " = T" + str(self._left._temp) + \
               str(self._oper) + "T" + str(self._right._temp)

    def execute(self, temps, stack, pc, sp):
        return eval(self._left + self._oper + self._right )
        #Instruction._temp += 1

