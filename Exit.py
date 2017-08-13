import Game
import Noun
class Exit(Noun.Noun):
    def __init__(self, desc, transistion, dest = None, locked=False, hidden=False):
        self.dest=dest
        self.desc=desc
        self.transistion=transistion
        self.locked = locked
        self.hidden = hidden
    def dummy():
        return Exit(None,None,None,True,True)
    def look(self):
        if self.desc:
            Game.say(self.desc)
        else:
            Game.say("There's nothing of interest")
    def travel(self):
        Game.curRoom = self.dest
        Game.say(self.transistion)
