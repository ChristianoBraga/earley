# https://anytree.readthedocs.io/en/latest/index.html
from anytree.importer import DictImporter
from anytree import RenderTree

importer = DictImporter()

def parseGrm(g):
    return {"S" : [["a","S","b"],["epsilon"]]}

def parse(g, w):
    return {"root" : "S",
            "children" : [{"root": "a"},
                          {"root" : "S",
                           "children" : [{"root": "a"}, {"root" : "b"}]},
                          {"root" : "b"}]}

def printDerivation(d):
    root = importer.import_(d)
    print(RenderTree(root))
    
    
