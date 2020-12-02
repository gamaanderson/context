import context

class Citation(context.ContextObject):
    def __init__(self, cite, reference=None):
      self.cite = cite
      self.reference = reference
      self.ans = self.ref

    @property
    def ref(self):
      if self.reference is None:
        return r"\cite{"+self.cite+r"}"
      else:
        return r"\cite["+self.reference+r"]{"+self.cite+r"}"

    @property
    def link(self):
      return r"\marginpar{"+self.ref+"}"
      return r"\footnote{"+self.ref+r"\hspace*{1cm} }"
