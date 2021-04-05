from sys import argv
from earley import parse, printDerivation, parseGrm

if  __name__ == "__main__":
    # Tratar existência dos parâmtros de entrada...
    printDerivation(parse(parseGrm(argv[1]), argv[2]))
