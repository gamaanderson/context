from context import Multi_string, ContextObject,  usepackage, Environment, ans
from babel_context import EQ

class Equation(Environment):
    abbreviation = EQ
    was_referenced = False

    def __init__(self, *args, ans=None, name=None, **kwargs):
        super().__init__(*args, **kwargs)
        if ans is not None:
            #self.ans += self.begin
            self.ans += ans
            #self.ans += self.end
        if name is not None:
          self._name = name
        else:
          self._name = "equation"
        self.ans.args = ("nomath",)

    @property
    def begin(self):
        return r"\begin{%s}\label{%i}" % (self.name, id(self))
    @property
    def end(self):
        return r"\end{%s}"%self.name
    @property
    def ref(self):
        self.was_referenced = True
        return r"%s (\ref{%i})" % (self.abbreviation, id(self))
    @property
    def link(self):
        self.was_referenced = True
        return r"\footnote{\ref{%i} \hspace*{1cm}}" % id(self)
    @property
    def name(self):
        if self.was_referenced:
            return self._name
        else:
            return self._name+"*"

def Math(*args, new=False, **kwargs):
    if len(args)==1:
        text = args[0]
        ### TODO correct inheritance bug
        if callable(text):
            if isinstance(text, MathFunction) and not new:
                return text
            return MathFunction(text, **kwargs)
        else:
            if isinstance(text, MathObject) and not new:
                return text
            return MathObject(text, **kwargs)
    elif len(args)>1:
        if isinstance(args, MathTuple):
            return args
        return MathTuple(args, **kwargs)


class MathFont(ContextObject):
    latex_command = [""]
    
    def __init__(self,text):
        super().__init__()
        self.text = text

    def __str__(self):
        return "{"+self.latex_command[0]+"{"+self.text+"}}"

class MathObject(ContextObject):
    ans = Multi_string()

    def __init__(self, text, name=None, definition=None, **kwargs):
        super().__init__()
        self.__str__= self._str_instance
        self.ans += text
        self.name=name
        self.ans.delimiter = " "
        self.definition = definition

    

    @classmethod
    def __str__(cls):
        return "INTERNAL ERROR _math.__init__.py"
        #return cls._latex_classmethod()

    def _str_instance(self):
        return self.latex()

    @property
    def long_name(self):
      return Math(self +":=" + self.definition)


    def latex(self, *args):
        if "nomath" not in args:
            args = args + ("math",)
        ans=self.ans
        return ans.latex(*args)

    @classmethod 
    def _latex_classmethod(cls, *args):
        if "nomath" not in args:
            args = args + ("math",)
        ans=cls.ans
        return ans.latex(*args)


class MathTuple(MathObject):
    def __init__(self, list_, **kwargs):
        super().__init__(list_[0],**kwargs)
        if len(list_)==2 and list_[1] is None:
            return
        for item in list_[1:]:
            self.ans += item
        self.ans.delimiter = ","
        
    def latex(self, *args):
        r=super().latex(*args)
        if "nomath" not in args:
            return "$("+r[1:-1]+")$"
        else:
            return "("+r+")"

class CallableMathObject(MathObject):
    def __init__(self, text, funct, name=None, **kwargs):
        super().__init__(text, **kwargs)
        self.function = funct

    def __call__(self, *args, **kwargs):
        return MathObject(self.function(*args, **kwargs))    

class MathFunction(ContextObject):
    def __init__(self, text, **kwargs):
        super().__init__()
        self.function = text

    def __call__(self, *args, **kwargs):
        return MathObject(self.function(*args, **kwargs))

    def latex(self, *args):
        return self.function.latex(*args)
