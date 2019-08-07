from . import Math,  MathObject, Multi_string

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

