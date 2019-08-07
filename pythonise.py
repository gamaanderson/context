# This Python file uses the following encoding: utf-8
import tokenize
import token as Token
import re
import sys

tokens=tokenize.generate_tokens(open(sys.argv[1]).readline)
p=re.compile(u'(§§|;\)|§[;\(\)]|§\.?[A-Za-z_0-9]*|[;\(\)])')


def pythonize(tokens):
    for token in tokens:
        if token[0] is not Token.STRING:
            yield token[0:2]
        else:
            #text = unicode(token[1], "utf-8")
            text = token[1]
            quot = text[0]
            text = text[1:-1]
            l = list(text)
            start = 0
            displace = 0
            #print(text)
            #print(l)
            previous = None
            for match in p.finditer(text):
                group = match.group(0)
                if group in (u"§§",u"§;",u"§(",u"§)"):
                    l.pop(match.start()+displace)
                    displace -= 1
                    pass
                elif group == u";)":
                    if start < match.start()+displace:
                        if  previous in ("NAME","STRING"):
                            yield (Token.OP, "+")
                        yield (Token.STRING, quot+"".join(l[start:match.start()+displace])+quot)#, token[2], token[3], token[4])
                    yield (Token.OP, ",")#, token[2], token[3], token[4])
                    yield (Token.NAME, "None")
                    yield (Token.OP, ")")
                    start = match.end()+displace
                    previous = "NAME"
                elif group == u";":
                    if start < match.start()+displace:
                        if  previous in ("NAME","STRING"):
                            yield (Token.OP, "+")
                        yield (Token.STRING, quot+"".join(l[start:match.start()+displace])+quot)#, token[2], token[3], token[4])
                    yield (Token.OP, ",")#, token[2], token[3], token[4])
                    start = match.end()+displace
                    previous = "OP"
                elif group == u"(":
                    if start < match.start()+displace:
                        if  previous in ("NAME","STRING"):
                            yield (Token.OP, "+")
                        yield (Token.STRING, quot+"".join(l[start:match.start()+displace])+quot)#, token[2], token[3], token[4])
                        previous = "STRING"
                    if  previous in ("STRING",):
                        yield (Token.OP, "+")
                    if  previous in ("STRING","OP", None):
                        yield (Token.NAME, "Math")
                    yield (Token.OP, "(")#, token[2], token[3], token[4])
                    start = match.end()+displace
                    previous = "OP"
                elif group == u")":
                    if start < match.start()+displace:
                        if  previous in ("NAME","STRING"):
                            yield (Token.OP, "+")
                        yield (Token.STRING, quot+"".join(l[start:match.start()+displace])+quot)#, token[2], token[3], token[4])
                    yield (Token.OP, ")")#, token[2], token[3], token[4])
                    start = match.end()+displace
                    previous = "NAME"
                elif match.group(0) == u"§":
                    continue
                elif match.group(0)[1] == u".":
                    #l.pop(match.start()+displace)
                    #displace -= 1
                    yield (Token.OP, ".")#, token[2], token[3], token[4])
                    yield (Token.NAME, "".join(l[match.start()+displace+2:match.end()+displace]))#, token[2], token[3], token[4])
                    start = match.end()+displace
                    previous = "NAME"
                else:
                    if start < match.start()+displace:
                        if  previous in ("NAME","STRING"):
                            yield (Token.OP, "+")
                        yield (Token.STRING, quot+"".join(l[start:match.start()+displace])+quot)#, token[2], token[3], token[4])
                        previous = "STRING"
                    #l.pop(match.start()+displace)
                    #displace -= 1
                    if  previous in ("NAME","STRING"):
                        yield (Token.OP, "+")
                    yield (Token.NAME, "".join(l[match.start()+displace+1:match.end()+displace]))#, token[2], token[3], token[4])
                    start = match.end()+displace
                    previous = "NAME"

            if l[start:]:
                if  previous in ("NAME","STRING"):
                    yield (Token.OP, "+")
                yield(Token.STRING, quot+"".join(l[start:])+quot)#, token[2], token[3], token[4])

py=pythonize(tokens)
#for k in py:
#    print k
print(tokenize.untokenize(py))


#def cut(tokens):
#    for token in tokens:
#        yield token[0:2]

#tokens=tokenize.generate_tokens(open("example.txt").readline)
#print(tokenize.untokenize(cut(tokens)))
