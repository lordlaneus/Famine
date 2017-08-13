import Noun
import Game
class Item(Noun.Noun):
    def __init__(self, name, desc, getable=True):
        Noun.Noun.__init__(self)
        self.name = name
        self.desc = desc
        self.getable = getable
    def look(self):
        Game.Game.say(self.desc)
    
