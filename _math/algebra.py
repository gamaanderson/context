from . import Math, category_theory

from .number_theory import Complexes
from .linear_algebra import LinearFont
from .category_theory import CategoryFont


Complex_Torus = Math(Complexes + "^*")

def _polyring(text, field=Complexes):
        return field + r"[" + text + "]"
polyring = Math(_polyring)

def _times(arg0, arg1):
        return arg0+"\\times "+arg1

times = Math(_times)

Group_Category =  category_theory.Category(CategoryFont("Grp"), object_font=LinearFont)
Ring_Category =  category_theory.Category(CategoryFont("Ring"), object_font=LinearFont)
Field_Category =  category_theory.Category(CategoryFont("Field"), object_font=LinearFont)