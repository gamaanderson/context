from context import ContextObject
import sys
import functools
import inspect

appendix = "_"

#BUG wenn Dokumente direkt im main datei gebildet wird, dann wir nichts importiert, das heißt sys.module funktiniert nicht.
#BUG verkurzung ref comfliktiert mit ref von modulen, also wie kann man sectionen referenzieren, sie werden auch nicht direkt gebildet, sondern nur durch doktorarbeit.py


class lazy_reference(ContextObject):
    def __init__(self, ref_string):
        super().__init__()
        self.ref_string = ref_string
        self.frame = inspect.currentframe().f_back.f_back
        if ref_string.startswith("."):
            frame= inspect.currentframe().f_back.f_back
            frameInfo = inspect.getframeinfo(frame)
            self.module_name = frameInfo.filename.split(".")[-2].split("/")[-1]
            self.path = ref_string.split(".")[1:]
        else:
            self.module_name = ref_string.split(".")[0]+appendix
            self.path = ref_string.split(".")[1:]
        #self.first_call = str(self)

    def __str__(self):
        if self.module_name in sys.modules.keys():
            mod = sys.modules[self.module_name]
            return functools.reduce(getattr, self.path+["ref"], mod)
        elif self.path:
            return r"\ref{"+str(self.path[-1])+r"}"
        else:
            return r"\ref{"+str(self.module_name)+r"}"


class lazy_link(ContextObject):
    def __init__(self, ref_string):
        super().__init__()
        self.ref_string = ref_string
        self.frame = inspect.currentframe().f_back.f_back
        if ref_string.startswith("."):
            frame= inspect.currentframe().f_back.f_back
            frameInfo = inspect.getframeinfo(frame)
            self.module_name = frameInfo.filename.split(".")[-2].split("/")[-1]
            self.path = ref_string.split(".")[1:]
        else:
            self.module_name = ref_string.split(".")[0]+appendix
            self.path = ref_string.split(".")[1:]

    def __str__(self):
        if self.module_name in sys.modules.keys():
            mod = sys.modules[self.module_name]
            return functools.reduce(getattr, self.path+["link"], mod)
        elif self.path:
            return r"\footnote{"+str(self.path[-1]).replace("_","\\_")+r" \hspace*{1cm}}"
        else:
            return r"\footnote{"+str(self.module_name).replace("_","\\_")+r" \hspace*{1cm}}"


list_refs = []

def ref(ref_string):
    aux = lazy_reference(ref_string)
    list_refs.append(aux)
    return aux

def link(ref_string):
    aux = lazy_link(ref_string)
    list_refs.append(aux)
    return aux

def call_all_refs():
    for element in list_refs:
      str(element)
