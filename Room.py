import Dir
from Exit import *
class Room:
    def __init__(self,name,desc):
        self.name = name
        self.desc = desc
        self.exits = [Exit.dummy()]*7
        self.inventory = []

    def addExit(self, direction, desc,trans,dest=None):
        self.exits[direction]=Exit(desc,trans,dest)
    def addItem(self, item):
        self.inventory.append(item)
    def addWall(self,direction,desc,trans):
        self.exits[direction]=Exit(desc,trans,None,True,True)
    def copyExit(self, d1, d2):
        self.exits[d2]=self.exits[d1]
    def countExits(self):
        count = 0
        for i in range(6):
            d = self.exits[i]
            if not d.hidden:
                count+=1
        return count
    def fullInventory(self):
        return self.inventory
    def listExits(self):
        out = ""
        for i in range(6):
            x= self.exits[i]
            if not x.hidden:
                out+= Dir.dirName(i)+", "
        
        return out
    def listInventory(self):
        inventory = self.inventory
        out = "You see: "
        if len(inventory)==0:
            return ""
        elif len(inventory)==1:
            return out + inventory[0].name
        else:
            for item in inventory:
                out+= item.name+", "
        out = out[0:-2]
        out = " and ".join(out.rsplit(" ",1))
        return out
    def remove(self,obj):
        self.inventory.remove(obj)
    def sayExits(self):
        count = self.countExits()
        if count==0:
            Game.say("There are no visible exits")
        elif count==1:
            Game.say("The only exit is " + self.listExits())
        else:
            Game.say("Exits are " +self.listExits())
    def look(self):
        Game.say(self.desc)
        Game.say(self.listInventory())
        self.sayExits()
