from s1c03 import solveS1C03, hexToBin

def solveS1C04(file):
    f =  open(file, "r")
    bestStrings = []
    for line in f:
        #remove newline
        line = line.rstrip()
        line = hexToBin(line.encode())
        solved = solveS1C03(line)
        bestStrings.append(solved)
    highest = max(bestStrings, key = lambda i : i[1])
    
    f.close()
    return highest[0]

