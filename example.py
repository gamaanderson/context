# This Python file uses the following encoding: utf-8
from context import *

from gamma import *
from latex import hyperref

ans += usepackage("geometry", margin="0.5in")

#opening
ans += title("Quotient Algebraische Varietäten")
ans += author("Gama, Anderson Luis")

with Document() as doc:

    ans += maketitle

    with Abstract():
        ans += "In diese Arbeit vergleichen wir 2 verschiedene Methode um Quotienten von algebraische Varietäten durch algebraische Gruppen Wirkung zu definieren. Der erste Methode ist die Geometrische Invariante Theorie (GIT), der an Hand eine Wahl teilt die Varietät in stabilen, instabilen und semi-stabilen Punkten, so dass die stabile Punkten ein geometrische Quotient haben und die semi-stabilen ein kategorischer Quotient. Der zweite Methode ist der Chow Quotient. Der nimmt einen ganz anderen Ziel, der Quotient ist weder ein subjektives Bild noch eine Parametrisierung von Bahnen, sondern ein Raum wo der Limit von Bahnen genommen werden kann. Wir sehen wie die kombinatorische Struktur, die hindert der Wahl von ein GIT Quotient steht, in dem Chow Quotient zusammengefasst wird.\n"

        ans += "Damit diese Diskussion nicht zu abstrakt bleibt arbeiten wird an Hand von zwei Beispiele, der eine, die torische Varietäten, explizit berechenbar, der zweite dagegen eher Praxis bezogen.\n"
    
    
    ans += section("Quotienten")

    ans += "Das Ziel einen Quotienten von Algebraische Varietäten durch Algebraische Gruppen zu bilden besteht dahin Bahnen zu parametrisieren. Versucht man jedoch den menge-theoretische Definition von Quotient einer Menge durch eine Relation zu verwenden, kommt man zu dem Ergebnis, dass der Quotient selten eine Algebraische  Varietät ist. Das ist unerwünscht.\n"

    ans += "Daher ist nötig eine andere Definition oder genauer: drei Definitionen"

    with Notation() as env:
        act = Math(lambda G,X: G+" \\circlearrowleft "+X)
        act.ans += "$"+ act("G","X")+"$"
        act.definition = env
        act.ref = env.ref

        ans += "Sei $X$ eine "+remind("algebraische Varietät")+", auf welcher eine" + remind("affine algebraische Gruppe")+"$G$"+remind("rational wirkt")+". Wir bezeichnen es bei"+define(act)

    with Definition() as de:
        ans += "Sei "+Math(Complexes+"[x_1,\ldots,x_n]")+" der Complexe Polynomring in $n$ Unbekannten und sei $I$ ein Primideal davon.  Eine" +define("affine algebraische Varietät")+"ist die Menge"+Set("x\in"+Complexes+"^n: f(x)=0 \\forall f\in I","X")+"ausgestattet mit der Menge ihrer regulären Funktionen."

        
    with Example():
         ans += "hi"

    with Notation():
         ans += "hi"

    ans += section("Quotienten")
	
    with Notation():
        ans += "hi"

    with Theorem():
        ans += "hi"

    with Example():
    	ans += "hi"

    with Notation() as no:
    	ans += "hi"
    ans += no.ref

    with Equation() as eq:
        ans +="\\int"
    ans+=eq.ref

print(ans)
