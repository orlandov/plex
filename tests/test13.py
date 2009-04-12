import Test
import sys
import types
from Plex import *
from StringIO import StringIO

digit = Range("09")
space = space = Any(" \t\n")

lex = Lexicon([
    (digit, 'digit'),
    (space, IGNORE)
])
f = StringIO("4\n2")
scanner = Scanner(lex, f)

i = scanner.tokens()
assert type(i) == types.GeneratorType
assert (list(i), [(4, 'digit'), (2, 'digit')])
