import context
from article import *
from theorem import *
from bibtex import Citation

context.usepackage("inputenc","utf8")
context.usepackage("fontspec")
context.usepackage("dutchcal")
context.usepackage("mathrsfs")
context.import_section += "\DeclareFontFamily{OT1}{pzc}{}\n \DeclareFontShape{OT1}{pzc}{m}{it}{<-> s * [1.15] pzcmi7t}{}\n \DeclareMathAlphabet{\mathpzc}{OT1}{pzc}{m}{it}\n"
context.usepackage("dsfont")

context.usepackage(
    "biblatex",backend="bibtex8", sortcites="true", bibstyle="alphabetic", citestyle="alphabetic",
    firstinits="true", useprefix="false",minnames="1", minalphanames="3", maxalphanames="4", maxbibnames="99",
    maxcitenames="3", natbib="true", eprint="true", url="true", doi="true", isbn="true", backref="true")
context.ans += "\\bibliography{references}"

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
    return r" \underline{%s} " % text
def remind(text):
    return " " + text + " "
def bold(text):
    return r"\bm{" + text + "}"

from _math import Equation
from _math.number_theory import Complexes, Reals, Integers, Rationals
from _math.number_theory import Naturals_with_0 as Naturals
from _math.algebra import polyring
from _math.algebraic_geometry import Affin, Projectiv, regularFunctions, picard, spec, Grassmanian
from _math.set_theory import Set
from _math.category_theory import isomorph
from _math.topology import closer
from _math.linear_algebra import dual
from _math import Math


def todo(text):
    return r"TODO: \textit{"+text+"}"

context.ans += r"\let\propsubset\subset"
context.ans += r"\renewcommand{\subset}{\subseteqq}"
context.ans += r"\let\propsupset\supset"
context.ans += r"\renewcommand{\supset}{\supseteqq}"

class Proof_idea(Proof):
    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      if self.theorem is not None:
        self.name = "Beweisidee von %s" % self.theorem.ref
      else:
        self.name = "Beweisidee"

act = r"\mathbin{\circlearrowleft}"

def define(text):
  return "\\textit{"+text+"}"

"""

\newcommand{\del}{\mathrm{d}}
\DeclareMathOperator{\sign}{sign}

\DeclareMathOperator{\rank}{rk}


"""
