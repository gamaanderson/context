import context

class Citation(context.ContextObject):
    def __init__(self, cite, reference=None):
      self.cite = cite
      self.reference = reference
      self.ans = self.ref

    @property
    def ref(self):
      if self.reference is None:
        return "\\cite{"+self.cite+"}"
      else:
        return "\\cite["+self.reference+"]{"+self.cite+"}"
