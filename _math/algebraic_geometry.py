from . import Math, Multi_string, CallableMathObject, category_theory, MathFont
from .linear_algebra import LinearFont
from .category_theory import Morphism, CategoryFont
from .algebra import Field_Category, Complexes

class SchemeFont(MathFont):
    latex_command = [""]

class SheafFont(MathFont):
    latex_command = [""]

class BboldFont(MathFont):
    latex_command = ["\\mathbb"]


Affin = Math(BboldFont("A"))
#Projectiv = Math(r"\mathbb{P}")
def _projectiv (text):
        return BboldFont("P")+"("+text+")"
Projectiv = CallableMathObject(BboldFont("P"),_projectiv)

class regularFunctions(category_theory.Morphism):
  ans = Multi_string((Math(SheafFont("O")),))
  def __init__(self, base=None,  **kwargs):
    if base is None:
        ans = SheafFont("O")
    else:
        ans = SheafFont("O")+"_{"+Math(base)+"}"
    super().__init__(ans)
    self.base = Math(base)


picard_group = Math(r"\text{Pic}")
picard = picard_group
def _spec(text):
        return SchemeFont("spec") + Math(text,None)
spec = Math(_spec)

def Grassmanian(r, V):
    return Math(SchemeFont("Gr")+Math(r,V))


def _dual(obj=""):
    return "{"+obj + "}^\\vee"
dual = Math(_dual)

field = Field_Category.Object("k")
Scheme_Category =  category_theory.Category(CategoryFont("Sch"),  object_font=SchemeFont)
Variety_Category =  category_theory.Category(CategoryFont("Var")+"_"+field, object_font=SchemeFont)
Complex_Variety_Category =  category_theory.Category(CategoryFont("Var")+"_"+Complexes, object_font=SchemeFont)

class Sheaf_cohomology(category_theory.Morphism):
  ans = Multi_string((Math(LinearFont("H")),))
  def __init__(self, order,  **kwargs):
    order = Math(order)
    ans = LinearFont("H")+"^"+order
    super().__init__(ans)
    self.order = order

symetric_algebra_sheaf = Morphism(SheafFont("Sym"))

endormophism_sheaf = lambda sheaf: Math(SheafFont("End")+Math(sheaf,None))
