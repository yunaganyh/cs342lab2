from s1c03 import solveS1C03 
from s1c02 import hexToBinary

def solveS1C04(file):
    f =  open(file, "r")
    bestStrings = []
    for line in f:
        #remove newline
        line = line.rstrip()
        line = hexToBinary(bytes(line, 'utf-8'))
        bestStrings.append(solveS1C03(line))

    highest = max(bestStrings, key = lambda i : i[1])
    
    f.close()
    return highest

