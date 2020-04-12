from context import ContextObject
import sys
import functools
import inspect

appendix = "_"

class lazy_reference(ContextObject):
    def __init__(self, ref_string):
        super().__init__()
        if ref_string.startwith("."):
            frame= inspect.currentframe().f_back
            frameInfo = inspect.getframeinfo(frame)
            self.module_name = frameInfo.filename.split(".")[-2]].split("/")[-1]
            self.path = ref_string.split(".")
        else:
            self.module_name = ref_string.split(".")[0]
            self.path = ref_string.split(".")[1:]

    def __str__(self):
        if self.module_name in sys.modules.keys():
            mod = sys.modules[self.module_name+self.appendix]
            return functools.reduce(getattr, self.path+["ref"], mod)
        elif self.path:
            return r"\ref{"+str(self.path[-1])+r"}"
        else:
            return r"\ref{"+str(self.module_name)+r"}"


class lazy_link(ContextObject):
    def __init__(self, ref_string):
        super().__init__()
        if ref_string.startwith("."):
            frame= inspect.currentframe().f_back
            frameInfo = inspect.getframeinfo(frame)
            self.module_name = frameInfo.filename.split(".")[-2]].split("/")[-1]
            self.path = ref_string.split(".")
        else:
            self.module_name = ref_string.split(".")[0]
            self.path = ref_string.split(".")[1:]

    def __str__(self):
        if self.module_name in sys.modules.keys():
            mod = sys.modules[self.module_name+self.appendix]
            return functools.reduce(getattr, self.path+["ref"], mod)
        elif self.path:
            return r"\footnote{"+str(self.path[-1])+r" \hspace*{1cm}}"
        else:
            return r"\footnote{"+str(self.module_name)+r" \hspace*{1cm}}"


def ref(ref_string):
    return lazy_reference(ref_string)

def link(ref_string):
    return lazy_link(ref_string)
