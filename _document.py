# This Python file uses the following encoding: utf-8
import context
 

class Document(context.Environment):
    begin = r"\begin{document}"
    end = r"\end{document}"


def title(_title):
    return "\\title{%s}" % _title

def author(_author):
    return "\\author{%s}" % _author

def section(_title):
    return "\\section{%s}" % _title


class Section(context.Environment):
    
    def __init__(self, title, silence=False):
        super().__init__(silence=silence)
        self.title = title
        self.begin = "\\section{%s}\label{%i}" % (title,id(self))
        self.end = ""

class Subsection(context.Environment):
    
    def __init__(self, title, silence=False):
        super().__init__(silence=silence)
        self.title = title
        self.begin = "\\subsection{%s}\label{%i}" % (title, id(self))
        self.end = ""
