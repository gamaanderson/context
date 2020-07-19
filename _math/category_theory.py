from . import Math, MathObject,CallableMathObject, MathFont

class CategoryFont(MathFont):
    latex_command = [""]

isomorph = Math(r"\cong")
hom_funktor = CallableMathObject(r"\mathtext{Hom}", lambda *args: Math("\hom")+tuple(args))#deprecated

hom = hom_funktor #deprecated

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
        return Math(s)

class Object(MathObject):
    category = ""

    @property
    def element_of(self):
        return Math(self+"\\in "+self.category)

class Category(MathObject):

    def __init__(self, text, *args, category_font=False, object_font=MathFont, morphism_font=MathFont, **kwargs):
        if category_font is True:
            text = CategoryFont(text)
        super().__init__(text, *args, **kwargs)
        self.object_font = object_font
        self.morphism_font = morphism_font


    def Object(self, name):
        obj = Object(self.object_font(name))
        obj.category = self
        return obj

    def Morphism (self, name, domane, codomane):
        mor = Morphism(self.morphism_font(name), domane, codomane)
        mor.category = self
        return mor
    
    def Hom_functor(self,domane, codomane):
        return Math(self.morphism_font("Hom")+Math(domane,codomane))

identity = Math(r"\mathrm{id}")
Set_Category = Category("Set", category_font=True)
