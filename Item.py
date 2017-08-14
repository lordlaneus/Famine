import Noun
import Game
class Item(Noun.Noun):
    def __init__(self, name, desc, getable=True, locked=True,putText="you can't place anything there"):
        Noun.Noun.__init__(self)
        self.name = name
        self.desc = desc
        self.getable = getable
        self.locked = locked
        self.putText= putText
        self.inText = "Contains: "
        self.inventory=[]
    def look(self):
        Game.Game.say(self.desc)
        Game.Game.say(self.showInventory())
    def put(self,obj):
        return self.putText.replace("@", obj.name)
    def fullInventory(self):
        out = []
        if not self.locked:
            for item in self.inventory:
                out.append(item)
                out+=item.fullInventory()
        return out
    def remove(self, obj):
        if obj in self.inventory:
            self.inventory.remove(obj)
        else:
            for item in self.inventory:
                if obj in item.fullInventory():
                    item.remove(obj)
    def showInventory(self):
        out = self.inText
        if not self.locked:
            for item in self.inventory:
                out+=item.name+", "

            out = out[0:-2]
            out = " and ".join(out.rsplit(", ",1))
            return out
       
        
