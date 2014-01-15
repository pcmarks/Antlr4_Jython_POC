__author__ = 'pcmarks'

from org.antlr.v4.runtime import ANTLRFileStream
from org.antlr.v4.runtime import CommonTokenStream
import RLexer
import RParser

import sys
print sys.argv[0]
print sys.argv[1]

ais = ANTLRFileStream(sys.argv[1])
lexer = RLexer(ais)
tokens = CommonTokenStream(lexer)
parser = RParser(tokens)
parser.setBuildParseTree(True)
tree = parser.prog()
tree.inspect(parser)
print tree.toStringTree(parser)
