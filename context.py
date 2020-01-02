# This Python file uses the following encoding: utf-8
import sys
import inspect
def latex(item, s, *args):
    try:
        if inspect.isclass(item):
            s.append(item._latex_classmethod(*args))
        else:
            s.append(item.latex(*args))
    except Exception as err:
        if isinstance(item,tuple):
            s.append("(")
            for item2 in item:
                latex(item2,s,*args)
                s.append(",")
            s[-1]=")"
        else:
            s.append(item.__str__())


class Multi_string(list):
    delimiter = "\n"
    args = ()

    def __add__(self, other):
        try:
            s = Multi_string(super().__add__(other))
            s.delimiter = self.delimiter
        except:
            s = Multi_string(self)
            s.append(other)
            s.delimiter = self.delimiter
        return s

    def __radd__(self, other):
        try:
            s = Multi_string(super().__radd__(other))
            s.delimiter = self.delimiter
        except:
            s = Multi_string(self)
            if type(other) is list:
                for i,item in enumerate(other):
                    s.insert(i, item)
            else:
                s.insert(0, other)
            s.delimiter = self.delimiter
        return s

    def __iadd__(self, other):
        try:
            super().__iadd___(other)
        except:
            self.append(other)
        return self

    def __str__(self):
        return self.latex()

    def latex(self, *args):
        s = []
        zirkumfix = ""
        args = args + self.args
        if "math" in args and "nomath" not in args:
            zirkumfix = "$"
            args = args + ("nomath",)
        for item in self:
            latex(item,s,*args)
        return zirkumfix + self.delimiter.join(s) + zirkumfix

class Ans():
    def __init__(self):
        self.ans = Multi_string()

    def __iadd__(self, other):
        try:
            self.ans += other
        except:
            self.ans.append(other)
        return self
    def __str__(self):
        return str(self.ans)
ans = Ans()
envoriment = None

import_section = Multi_string()

def usepackage(package, *args,  Info=None, **kwargs):
    ops = ""
    for arg in args:
        ops+="%s," % arg
    for key in kwargs.keys():
        ops += "%s=%s," % (key, kwargs[key])

    if Info is None:
      import inspect
      frame= inspect.currentframe().f_back
      frameInfo = inspect.getframeinfo(frame)

      Info = "%s:%s"%(frameInfo.filename, frameInfo.lineno)

    global import_section

    import_section += "\\usepackage[%s]{%s} "%(ops, package)+r"%" + "%s"% (Info)
# in article.py context.ans += context.import_section


class _ContextObject():
    def __init__(self):
        self.ans = Multi_string()
    
    def __str__(self):
        return str(self.ans)

    def __add__(self, other):
        s =  Multi_string((self, other))
        s.delimiter = ""
        return s

    def __radd__(self, other):
        s = Multi_string((other, self))
        s.delimiter = ""
        return s





class _fabric(type):
    
    def __add__(self, other):
        s =  Multi_string((self, other))
        s.delimiter = ""
        return s

    def __radd__(self, other):
        s = Multi_string((other, self))
        s.delimiter = ""
        return s

ContextObject = _fabric("ContextObject",(_ContextObject,),{})



class DocumentClass(ContextObject):
    def __init__(self, className, **kwargs):
        super().__init__()
        self.className = className
        self.kwargs = kwargs

    def __str__(self):
        ops = ""
        for key in self.kwargs.keys():
            ops += "%s," % (self.kwargs[key])
        return "\\documentclass[%s]{%s}" % (ops,self.className)

class Environment(ContextObject):
    begin = ""
    end = ""
    father_envoriment = None


    def __init__(self, silence=False, **kwargs):
        super().__init__()
        self.silence = silence
        

    def __enter__(self):
        global ans
        global envoriment
        #self.ans += self.begin
        self._save_ans = [ans.ans]
        ans.ans= self.ans
        self.father_envoriment = envoriment
        envoriment = self
        return self
        
    def __exit__(self, type, value, traceback):
        global ans
        global envoriment
        #self.ans += self.end
        ans.ans = self._save_ans.pop()
        envoriment = self.father_envoriment
        if self.silence is False:
            ans += self

    def __str__(self):
        return str(Multi_string((self.begin,self.ans, self.end)))

    @property
    def ref(self):
        return r"\ref{%i}" % (id(self))

class itemize(Environment):
    def __init__(self, type_="itemize", silence=False):
        super().__init__(silence)
        self.begin = "\\begin{"+type_+"}"
        self.end = "\\end{"+type_+"}"

    def __call__(self, text=""):
        self.ans += "\item " + text



class table(Environment):
    def __init__(self, form, type_="tabular", hline=True, silence=False):
        super().__init__(silence)
        self.hline = "True"
        self.begin = "\\begin{"+type_+"}{"+form+"}"
        if self.hline:
          self.end = "\\hline \n \\end{"+type_+"} \n"
        else:
          self.end = "\\end{"+type_+"}"

    def __call__(self, *cols):
        if self.hline:
          line = "\\hline "
        else:
          line = ""
        if len(cols)>=1:
          line += cols[0]
        if len(cols)>1:
          for col in cols[1:]:
            line += " & "+ col
        line += r" \\"
        self.ans += line

