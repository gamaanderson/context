# This Python file uses the following encoding: utf-8
import context
from _document import Document, title, author, section, Subsection, Section, Paragraph

documentClass = context.DocumentClass("article")
context.ans += documentClass
context.ans += context.import_section
maketitle = r"\maketitle"

class Abstract(context.Environment):
    begin = r"\begin{abstract}"
    end = r"\end{abstract}"
