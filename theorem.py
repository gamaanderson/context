# This Python file uses the following encoding: utf-8
import context

from latex import amssymb, amsthm, thmtools, amsmath
import babel_context as babel

context.usepackage("footmisc","para", "perpage")
context.ans += "\\let\\oldfootnote\\footnote\n\\def\\footnote{\\ifhmode\\unskip\\fi\\oldfootnote}"

class _dynamic_string():
    def __init__(self, string):
        self.string = string
    def __str__(self):
        return self.string

class Proof_deprecated(context.Environment):
    name = "proof"
    begin = r"\begin{proof}"
    end = r"\end{proof}"
    def __init__(self, theorem, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.theorem = theorem

    def __call__(self, silence):
        self.silence = silence
        return self

latex_styles = {"italic": r"\itshape"}

context.ans += r"\newcounter{theorem}[section]"
context.ans += r"\renewcommand{\thetheorem}{\thesection.\arabic{theorem}}"

context.ans += r"\newcounter{subtheorem}[theorem]"
context.ans += r"\renewcommand{\thesubtheorem}{\thetheorem.\arabic{subtheorem}}"




class _basetheorem(context.Environment):
    theorem_end = None
    counter = "theorem"
    label_counters = ("section", "theorem")
    environment = "textbf"
    formation = ""
    style = ()

    def __init__(self, name=None, subname=None, ans=None, theorem=None, proof=False, proof_type = "long", **kwargs):
        super().__init__(**kwargs)
        self.dependences = []
        if ans is not None:
            #self.ans += self.begin
            self.ans += ans
            #self.ans += self.end
        self.subtheorems = []
        if theorem is None:
          if proof_type == "long":
              self.proof = Proof(theorem=self)
          else:
              self.proof = Short_proof(theorem=self)
              proof = True
        else:
          self.theorem = theorem
          if isinstance(theorem, Definition):
            self.name = babel.WELLDEFINITION_OF +" %s" % theorem.ref
          else:
            self.name = babel.PROOF_OF+" %s" % theorem.ref
        if name is not None:
            self.name = name
        if subname is not None:
            self.name += ": "+subname
        self.proof_link = proof or (proof_type is not "long")

    def __enter__(self):
        super().__enter__()
        if issubclass(self.father_envoriment.__class__, _basetheorem):
            self.father_envoriment.subtheorems.append(self) 
        return self

    @property
    def begin(self):
        aux = r"\refstepcounter{%s}" %  self.counter
        aux += r"\newline\%s{" % self.environment
        for counter in self.label_counters:
            aux += r"\arabic{%s}." % counter
        if aux[-1] is ".":
                aux=aux[:-1]
        if self.dependences:
          if len(self.dependences) == 1:
            ###TODO implement babel
            aux += "\\protect\\footnote{Hängt von "+self.dependences[0].ref+" ab}"
          elif len(self.dependences) == 2:
            aux += "\\protect\\footnote{Hängt von "+self.dependences[0].ref+" und "+self.dependences[1].ref+" ab}"
          else:
            aux1 = "\\protect\\footnote{Hängt von "
            for dep in self.dependences[:-2]:
              aux1 += dep.ref+", "
            aux1 += self.dependences[-2].ref+" und "+self.dependences[-1].ref+" ab}"
            aux += aux1
        #if self.proof_link:
        #    aux += r"\protect" + self.proof.link
        aux += r") %s} \label{%i}""\n" % (self.name, id(self))
        aux += r"{"
        aux += self.formation
        for style in self.style:
            aux += "%s " % latex_styles[style]    
        return aux

    @property
    def end(self):
        if self.theorem_end is None:
            aux = "\n"
        else:
            aux = " \hfill %s\n\n" % self.theorem_end
        if self.proof_link:             
            if isinstance(self.proof, Proof):
                if isinstance(self, Definition):
                    aux += r"\protect \textit{"+babel.TO_WELLDEFINITION+": }" + self.proof.ref + "\n\n"
                else:
                    aux += r"\protect \textit{"+babel.TO_PROOF+": }" + self.proof.ref + "\n\n"
            else:
                if isinstance(self, Definition):
                    aux += r"\protect \textit{"+babel.TO_WELLDEFINITION+": }" + self.proof + "\n\n"
                else:
                    aux += r"\protect \textit{"+babel.TO_PROOF+": }" + self.proof + "\n\n"
            
        aux += "}\n\n"
        return aux

class _theorem_fabric(context._fabric):
    
    def __new__(cls, name, bases, _dict):
        _dict["name"] = name

        _dict["ref"] = property(lambda self: r"\ref{%i}" % id(self))
        _dict["link"] = property(lambda self: r"\footnote{\ref{%i} \hspace*{1cm}}" % id(self))
        return super().__new__(cls, name, bases, _dict)


#class factory
def newtheorem(name, style=(), theorem_end=None, **kwargs):
    arg = r""
    # metaclass magics
    return _theorem_fabric(name,(_basetheorem,), {"style":style,"theorem_end":theorem_end})

Theorem = newtheorem(babel.THEOREM)
Conjecture = newtheorem(babel.CONJECTURE)
Observation = newtheorem(babel.OBSERVATION)
Lemma = newtheorem(babel.LEMMA)
Affirmation = newtheorem(babel.AFFIRMATION)
Proposition = newtheorem(babel.PROPOSITION)
Corollary = newtheorem(babel.COROLLARY)

Notation = newtheorem(babel.NOTATION,)
Definition = newtheorem(babel.DEFINITION,theorem_end=r"$\Diamond$")
Example = newtheorem(babel.EXAMPLE,theorem_end=r"$\Diamond$")
Subtheorem = newtheorem("")
Subtheorem.label_counters = ("section", "theorem", "subtheorem")
Subtheorem.counter = "subtheorem"
Subtheorem.environment = "subparagraph"
Subtheorem.formation = r"\setlength{\leftskip}{0.6cm}"

Proof = newtheorem(babel.PROOF,theorem_end=r"$\qedsymbol$")

class Short_proof(context.Environment):
    theorem_end = r"$\qedsymbol$"

    def __init__(self, *args, theorem=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.theorem = theorem
        self.silence = True
        self.end = "\hfill "+self.theorem_end

#    @property
#    def ref(self):
#      return self.ans+"\hfill"+self.theorem_end

context.ans += r"\usepackage{titlesec}"
context.ans += r"\titlespacing{\subparagraph}{0pt}{0pt}{1em}"





def remide(*args):
    print(r"\remind{%s}"%",".join(args))

