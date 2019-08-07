from . import Math, MathObject,CallableMathObject


isomorph = Math(r"\cong")
hom_funktor = CallableMathObject(r"\hom", lambda *args: Math("\hom")+tuple(args))

hom = hom_funktor

class Morphism(MathObject):
    category = ""
    
    def __init__(self,name=None,domane=None,codomane=None):
        super().__init__(name)
        self.domane = domane
        self.codomane = codomane
    
    @property
    def long_name(self):
        return Math(self+":"+self.domane+"\\to "+self.codomane)

    @property
    def element_of(self):
        return Math(self+"\\in "+hom_funktor+"("+self.domane+","+self.codomane+")")
    
    def __call__(self, *args):
        s = self+"("
        for arg in args:
            s+=arg
            s+=","
        s[-1]=")"
        return s

class Object(MathObject):
    category = ""

    @property
    def element_of(self):
        return Math(self+"\\in "+self.category)

class Category(MathObject):
    def Object(self, name):
        obj = Object(name)
        obj.category = self
        return obj

    def Morphism (self, name, domane, codomane):
        mor = Morphism(name, domane, codomane)
        mor.category = self
        return mor

identity = Math(r"\text{id}")
Set_Category = Category("\\mathrm{Set}")
