from . import Math, CallableMathObject
from .number_theory import Complexes

def dual(text):
    return text+"^*"

def _direct_sum(arg0, arg1):
        return arg0+"\\oplus "+arg1

direct_sum = Math(_direct_sum)

def _tensor(arg0, arg1):
        return arg0+"\\otimes "+arg1

tensor = CallableMathObject("\\otimes", _tensor)

def _general_linear_group(field=Complexes, size="n"):
        if size:
          return "\\text{GL}_"+size+"("+field+")"
        else:
          return "\\text{GL}"+"("+field+")"
general_linear_group = Math(_general_linear_group)

def _projectiv_general_linear_group(field=Complexes, size="n"):
        if size:
          return "\\text{PGL}_"+size+"("+field+")"
        else:
          return "\\text{PGL}"+"("+field+")"
projectiv_general_linear_group = Math(_projectiv_general_linear_group)

def _special_linear_group(field=Complexes, size="n"):
        if size:
          return "\\text{SL}_"+size+"("+field+")"
        else:
          return "\\text{SL}"+"("+field+")"
special_linear_group = Math(_special_linear_group)

def _projectiv_special_linear_group(field=Complexes, size="n"):
        if size:
          return "\\text{PSL}_"+size+"("+field+")"
        else:
          return "\\text{PSL}"+"("+field+")"
projectiv_special_linear_group = Math(_projectiv_special_linear_group)

def _unitary_linear_group(field=Complexes, size="n"):
        if size:
          return "\\text{U}_"+size+"("+field+")"
        else:
          return "\\text{U}"+"("+field+")"
unitary_linear_group = Math(_unitary_linear_group)



def _matrixes(ring=Complexes, size="n"):
        return "\\text{M}_"+size+"("+ring+")"
Matrixes = Math(_matrixes)
