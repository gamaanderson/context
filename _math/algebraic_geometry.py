from . import Math, Multi_string, CallableMathObject, category_theory


Affin = Math(r"\mathbb{A}")
#Projectiv = Math(r"\mathbb{P}")
def _projectiv (text):
        return r"\mathbb{P}"+"("+text+")"
Projectiv = CallableMathObject(r"\mathbb{P}",_projectiv)
        
class regularFunctions(category_theory.Morphism):
  ans = Multi_string(("\\mathcal{O}",))
  def __init__(self, base=None,  **kwargs):
    if base is None:
        ans = "\\mathcal{O}"
    else:
        ans = "\\mathcal{O} _"+Math(base)
    super().__init__(ans)
    self.base = Math(base)


picard_group = Math(r"\text{Pic}")
picard = picard_group
def _spec(text):
        return r"\text{spec } " + text
spec = Math(_spec)

def Grassmanian(r, V):
    return Math(r"\text{Gr}(%s,%s)" % (r,V))


def _dual(obj=""):
    return "{"+obj + "}^\\vee"
dual = Math(_dual)
