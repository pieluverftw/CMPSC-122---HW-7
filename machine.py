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
    def __init__ (self, value):
        self._temp = value
    #Instruction._temp += 1

    def compute(self):
        return eval(str(self._temp))
    # /test

    pass

class Load (Instruction):
    def __init__(self, var, variables):
        val = variables.lookup(var)
        Instruction.__init__(self, val)

    def compute(self):
        return eval(str(self._temp))

    # test
    # temp[t]= v1
    # Instruction._temp += 1
    # /test

class Store(Instruction):
    def __init__(self, instr, var, variables):
        variables.assign(var, instr.compute())          # instr not yet defined

    def compute(self):
        return
    # test
    #stack.push(temp[t]0)
    #Instruction._temp += 1
    #return
    # /test

class Compute(Instruction)
    def __init__ (self, l, op, r):
        self._left = l
        self._oper = op
        self._right = r
    def compute(self):
        return eval(left + oper + right )
        #Instruction._temp += 1
