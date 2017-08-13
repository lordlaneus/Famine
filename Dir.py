N = 0
S = 1
E = 2
W = 3
U = 4
D = 5
B = 6
fullNameTable = ["north", "south","east","west","up","down","back"]
shortNameTable ="nsewudb"
def strToDir(d):
  
    out = shortNameTable.find(d)
    if out<0:
        if d in fullNameTable:
            out= fullNameTable.index(d)
    return out
