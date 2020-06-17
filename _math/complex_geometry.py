from . import Math,  MathObject, CallableMathObject, Multi_string, MathFont, number_theory, category_theory
from .linear_algebra import LinearFont


class ComplexFont(MathFont):
    latex_command = [""]

from .differential_geometry import Forms_bundle

endomorphism_bundle = lambda bundle: Math(ComplexFont("End")+Math(bundle,None))


class Dolbeault_cohomology(category_theory.Morphism):
  ans = Multi_string((Math(LinearFont("H")),))
  def __init__(self, order,  **kwargs):
    order = Math(order)
    ans = LinearFont("H")+"^{"+order+"}"
    super().__init__(ans)
    self.order = order
