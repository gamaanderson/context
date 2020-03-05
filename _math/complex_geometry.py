from . import Math,  MathObject, CallableMathObject, Multi_string, MathFont, number_theory



class ComplexFont(MathFont):
    latex_command = [""]

from .differential_geometry import Forms_bundle

endormophism_bundle = lambda bundle: Math(ComplexFont("End")+Math(bundle,None))
