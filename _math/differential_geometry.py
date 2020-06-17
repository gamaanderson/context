from . import Math,  MathObject, CallableMathObject, Multi_string, MathFont, number_theory, category_theory
from .linear_algebra import LinearFont


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

class Forms_bundle(MathObject):
  def __init__(self, manifold, degree=None,  **kwargs):
    if degree is None:
      ans = "\Omega ("+Math(manifold)+")"
    else:
      ans = "\Omega^{"+Math(degree)+"} ("+Math(manifold)+")"
    super().__init__(ans)
    self.manifold = Math(manifold)
    self.degree = Math(degree)

class Tangent_Space(MathObject):
  def __init__(self, manifold, base_point=None, **kwargs):
    if base_point is None:
      ans = "T "+manifold
    else:
      ans = "T_{"+base_point+"} "+manifold
    super().__init__(ans)
    self.manifold = Math(manifold)
    self.base_point = Math(base_point)

class Cotangent_Space(MathObject):
  def __init__(self, manifold, base_point=None, **kwargs):
    if base_point is None:
      ans = "T^* "+manifold
    else:
      ans = "T^*_{"+base_point+"} "+manifold
    super().__init__(ans)
    self.manifold = Math(manifold)
    self.base_point = Math(base_point)

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


endormophism_bundle = lambda bundle: Math(DifferentialFont("End")+Math(bundle,None))


class DeRahm_cohomology(category_theory.Morphism):
  ans = Multi_string((Math(LinearFont("H")),))
  def __init__(self, order,  **kwargs):
    order = Math(order)
    ans = LinearFont("H")+"_{dR}"+"^{"+order+"}"
    super().__init__(ans)
    self.order = order
