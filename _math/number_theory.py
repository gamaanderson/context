from . import Math, MathFont

class BboldFont(MathFont):
    latex_command = ["\\mathbb"]

Complexes = Math(BboldFont("C"))
ImaginaryI = Math(r"\mathrm{i}")
Reals = Math(BboldFont("R"))
Rationals = Math(BboldFont("Q"))
Integers = Math(BboldFont("Z"))

Naturals_with_0 = Math(BboldFont("N"))
Naturals_with_0.description = "Naturals with 0"

Naturals_without_0 = Math(BboldFont("N"))
Naturals_without_0.description = "Naturals without 0"

Naturals = Naturals_without_0

Unitary_complexes = Math(BboldFont("S")+ "^1")