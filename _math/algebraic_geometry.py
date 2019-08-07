from . import Math, CallableMathObject

Affin = Math(r"\mathbb{A}")
#Projectiv = Math(r"\mathbb{P}")
def _projectiv (text):
        return r"\mathbb{P}"+"("+text+")"
Projectiv = CallableMathObject(r"\mathbb{P}",_projectiv)
        
regularFunctions = Math(r"\mathcal{O}")
picard_group = Math(r"\text{Pic}")
picard = picard_group
def _spec(text):
        return r"\text{spec } " + text
spec = Math(_spec)

def Grassmanian(r, V):
    return Math(r"\text{Gr}(%s,%s)" % (r,V))

