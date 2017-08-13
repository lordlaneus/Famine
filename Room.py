import Dir
from Exit import *
class Room:
    def __init__(self,name,desc):
        self.name = name
        self.desc = desc
        self.exits = [Exit.dummy()]*7

    def addExit(self, direction, desc,trans,dest=None):
        self.exits[direction]=Exit(desc,trans,dest)
    def listExits():
        return "NO EXIT"
    def look(self):
        out = self.desc+"\n"
        out +=self.listExits()
        return out
