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
    
    def __init__(self, title, short_title=None, numbered=True, silence=False):
        super().__init__(silence=silence)
        self.title = title
        if numbered:
          name = "\\section"
        else:
          name = "\\section*"
        if short_title is None:
            self.begin = name + "{%s}\label{%i}" % (title,id(self))
        else:
            self.begin = name + "[%s]{%s}\label{%i}" % (short_title,title,id(self))
        self.end = ""

class Subsection(context.Environment):
    
    def __init__(self, title, numbered=True, silence=False):
        super().__init__(silence=silence)
        self.title = title
        if numbered:
          name = "\\subsection"
        else:
          name = "\\subsection*"
        self.begin = name + "{%s}\label{%i}" % (title, id(self))
        self.end = ""
