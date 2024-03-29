import context
from article import *
from theorem import *
from lazy_referenz import ref, link
from bibtex import Citation

context.usepackage("mathtools")
context.usepackage("inputenc","utf8")
context.usepackage("fontspec")


context.usepackage(
    "biblatex",backend="bibtex8", sortcites="true", bibstyle="alphabetic", citestyle="alphabetic",
    firstinits="true", useprefix="false",minnames="1", minalphanames="3", maxalphanames="4", maxbibnames="99",
    maxcitenames="3", natbib="true", eprint="true", url="false", doi="true", isbn="true", backref="true", sorting="ynt")
context.ans += "\\bibliography{references}"
# https://tex.stackexchange.com/questions/200997/underlined-titles-in-bibliography-with-biblatex-and-ulem-packages
#context.ans += "\\DeclareFieldFormat*{title}{#1}"
#context.ans += "\\DeclareFieldFormat*{titlecase}{%\n\\ifdef{\\currentfield}\n{\\ifcurrentfield{title}\n{\\usefield{\\uline}{\\currentfield}}%\n{#1}}\n{#1}}"

context.ans += r"\setlength{\parindent}{0em}"
context.ans += r"\setlength{\parskip}\bigskipamount"



context.ans += r"\swapnumbers"
context.ans += r"\renewcommand*{\thefootnote}{\alph{footnote}}"

Theorem.definition = r"\declaretheorem[style=theorem,numberwithin=section]{theorem}"
Observation.definition = r"\declaretheorem[style=theorem,sibling=theorem]{observation}"
Lemma.definition = r"\declaretheorem[style=theorem,sibling=theorem]{lemma}"
Affirmation.definition = r"\declaretheorem[style=theorem,sibling=theorem]{affirmation}"
Proposition.definition = r"\declaretheorem[style=theorem,sibling=theorem]{proposition}"
Corollary.definition = r"\declaretheorem[style=theorem,sibling=theorem]{corollary}"
Notation.definition = r"\declaretheorem[style=definition,sibling=theorem]{notation}"
Definition.definition = r"\declaretheorem[style=definition,qed=$\Diamond$,sibling=theorem]{definition}"
Example.definition = r"\declaretheorem[style=definition,qed=$\Diamond$,sibling=theorem]{example}"


def define(text):
    return r" \textit{"+ text+"}"
def remind(text):
    return " " + text + " "
def bold(text):
    return r"\bm{" + text + "}"

from _math import Equation
from _math.number_theory import Complexes, Reals, Integers, Rationals
from _math.number_theory import Naturals_with_0 as Naturals
from _math.algebra import polyring
from _math.algebraic_geometry import Affin, Projectiv, regularFunctions, picard, spec, Grassmannian
from _math.set_theory import Set
from _math.category_theory import isomorph
from _math.topology import closer
from _math.linear_algebra import dual
from _math import Math


def todo(text):
    return r"TODO: \textit{"+text+"}"

context.ans += r"\let\propsubset\subset"
context.ans += r"\renewcommand{\subset}{\subseteq}"
context.ans += r"\let\propsupset\supset"
context.ans += r"\renewcommand{\supset}{\supseteq}"
context.ans += r"\newcommand{\xto}[1]{\xrightarrow{#1}}"
context.ans += r"\renewcommand{\xmapsto}[1]{\mapsto^{#1}}"



class _Proof_idea(Proof):
    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      if self.theorem is not None:
        self.name = "Idea of the proof for %s" % self.theorem.ref
      else:
        self.name = "Idea of the proof"

class _Short_proof_idea(Short_proof):
    def __init__(self, *args, theorem=None, **kwargs):
      super().__init__(*args, **kwargs)
      self.theorem = theorem
      self.ans += r"\protect \textcolor{red}{\textit{Idea of the proof:}}"

def Proof_idea(*args, proof_type="long", **kwargs):
    if proof_type is "long":
      return _Proof_idea(*args,**kwargs)
    else:
      return _Short_proof_idea(*args,**kwargs)

act = r"\mathbin{\circlearrowleft}"

GIT = "GIT"

"""

\newcommand{\del}{\mathrm{d}}
\DeclareMathOperator{\sign}{sign}

\DeclareMathOperator{\rank}{rk}


"""
