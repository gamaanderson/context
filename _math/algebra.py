from . import Math

from .number_theory import Complexes

Complex_Torus = Math(Complexes + "^*")

def _polyring(text, field=Complexes):
        return field + r"[" + text + "]"
polyring = Math(_polyring)

def _times(arg0, arg1):
        return arg0+"\\times "+arg1

times = Math(_times)

