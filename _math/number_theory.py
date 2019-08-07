from . import Math

Complexes = Math(r"\mathbb{C}")
ImaginaryI = Math(r"\mathrm{i}")
Reals = Math(r"\mathbb{R}")
Rationals = Math(r"\mathbb{Q}")
Integers = Math(r"\mathbb{Z}")

Naturals_with_0 = Math(r"\mathbb{N}")
Naturals_with_0.description = "Naturals with 0"

Naturals_without_0 = Math(r"\mathbb{N}")
Naturals_without_0.description = "Naturals without 0"

Naturals = Naturals_without_0

