from . import Math, CallableMathObject, MathFont
from .number_theory import Complexes
from .category_theory import  Morphism

class LinearFont(MathFont):
    latex_command = ["\\text"]


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
          return LinearFont("GL")+"_"+size+"("+field+")"
        else:
          return LinearFont("GL")+"("+field+")"
general_linear_group = Math(_general_linear_group)

def _projectiv_general_linear_group(field=Complexes, size="n"):
        if size:
          return  LinearFont("PGL")+"_"+size+"("+field+")"
        else:
          return  LinearFont("PGL")+"("+field+")"
projectiv_general_linear_group = Math(_projectiv_general_linear_group)

def _special_linear_group(field=Complexes, size="n"):
        if size:
          return  LinearFont("SL")+"_"+size+"("+field+")"
        else:
          return  LinearFont("SL")+"("+field+")"
special_linear_group = Math(_special_linear_group)

def _projectiv_special_linear_group(field=Complexes, size="n"):
        if size:
          return  LinearFont("PSL")+"_"+size+"("+field+")"
        else:
          return  LinearFont("PSL")+"("+field+")"
projectiv_special_linear_group = Math(_projectiv_special_linear_group)

def _unitary_linear_group(field=Complexes, size="n"):
        if size:
          return  LinearFont("U")+"_"+size+"("+field+")"
        else:
          return  LinearFont("U")+"("+field+")"
unitary_linear_group = Math(_unitary_linear_group)



def _matrixes(ring=Complexes, size="n"):
        return LinearFont("M")+"_"+size+"("+ring+")"
Matrixes = Math(_matrixes)

symetric_algebra = Morphism(LinearFont("Sym"))

one_morphism =  Morphism("1")
