from . import Math,  MathObject, CallableMathObject, Multi_string, MathFont, number_theory



class DifferentialFont(MathFont):
    latex_command = [""]

class C_Font(MathFont):
    latex_command = [""]

class EichFont(MathFont):
    latex_command = [""]

class Forms(MathObject):
  def __init__(self, manifold, degree=None,  **kwargs):
    if degree is None:
      ans = "\Omega ("+Math(manifold)+")"
    else:
      ans = "\Omega^{"+Math(degree)+"} ("+Math(manifold)+")"
    super().__init__(ans)
    self.manifold = Math(manifold)
    self.degree = Math(degree)


class Sections(MathObject):
  ans = Multi_string(("\\Gamma",))
  def __init__(self, bundle,  **kwargs):
    ans = "\\Gamma ("+Math(bundle)+")"
    super().__init__(ans)
    self.bundle = Math(bundle)


class C_differential_class(MathObject):
  ans = Multi_string((C_Font("C"),))
  def __init__(self, order ,  **kwargs):
    order = Math(order)  
    ans = C_Font("C")+"^"+order
    super().__init__(ans)
    self.order = order

C_infinity = C_differential_class("\\infty")

def _projectiv (text):
        return number_theory.BboldFont("P")+"("+text+")"
Projectiv = CallableMathObject(number_theory.BboldFont("P"),_projectiv)
