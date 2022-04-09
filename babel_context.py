 
PROPOSITION = "Satz"
CONJECTURE = "Vermutung"
THEOREM = "Hauptsatz"
LEMMA = "Hilfsatz"
COROLLARY = "Folgerung"
OBSERVATION = "Bemerkung"
AFFIRMATION = "Behauptung"
NOTATION = "Bezeichnung"
DEFINITION = "Definition"
EXAMPLE = "Beispiel"
PROOF = "Beweis"
TO_PROOF = "Zum Beweis"
PROOF_OF = "Beweis von"
WELLDEFINITION_OF = "Wohldefiniertheit von"
TO_WELLDEFINITION = "Zur Wohldefiniertheit"
EQ = "Gl."
QUESTION = "Frage"
ANSWER = "Antwort"
ANSWER_TO = "Antwort zu"


_language = "deutsch"

def set_language (lang="deutsch"):
  global PROPOSITION
  global CONJECTURE
  global THEOREM 
  global LEMMA
  global COROLLARY 
  global OBSERVATION
  global AFFIRMATION
  global NOTATION 
  global DEFINITION
  global EXAMPLE
  global PROOF 
  global TO_PROOF 
  global PROOF_OF 
  global WELLDEFINITION_OF
  global TO_WELLDEFINITION
  global EQ 
  global QUESTION
  global ANSWER
  global ANSWER_TO

  if lang == "english":    
    PROPOSITION = "Proposition"
    CONJECTURE = "Conjecture"
    THEOREM = "Theorem"
    LEMMA = "Lemma"
    COROLLARY = "Corollary"
    OBSERVATION = "Observation"
    AFFIRMATION = "Assertion"
    NOTATION = "Notation"
    DEFINITION = "Definition"
    EXAMPLE = "Example"
    PROOF = "Proof"
    TO_PROOF = "For the proof"
    PROOF_OF = "Proof of"
    WELLDEFINITION_OF = "Well definition of "
    TO_WELLDEFINITION = "To the well definition"
    EQ = "eq."
    QUESTION = "Question"
    ANSWER = "Answer"
    ANSWER_TO = "Answer to"

    
  elif lang == "deutsch":
    pass # no change
  else:
    import warnings
    warnings.warn("Language not defined, staying with german")
