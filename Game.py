from Room import *
import Dir
map = []
prompt = "It's A Cold Day In Hell"
bunker = Room("bunker", "A dusty old bunker")
surface = Room("surface", "Everything is dead.")

bunker.addExit(Dir.U,"A rusty ladder leads up","You ascend the ladder to the surface.",surface,)
surface.addExit(Dir.D,"An unremarkable hatch lies beneath you.","You return to your bunker.",bunker) 
surface.addExit(Dir.U,"The sky is obscured by a thick layer of smog.","Try as you might, you fail to break your earthly tether.") 

map.append(bunker)
map.append(surface)
curRoom = bunker

def say(s):
    global prompt
    prompt+=s+"\n"
    
def findNoun(noun):
    d = Dir.strToDir(noun)
    if d>-1:
        return Game.curRoom.exits[d]
    else:
        return None
        
def travel(direction):
    if not curRoom.exits[direction].locked:
        curRoom.exits[direction].travel()
    elif curRoom.exits[direction].transistion:
        Game.say(curRoom.exits[direction].transistion)
    else:
        Game.say("you can't go that way")
def look(obj):
    if obj:
       obj.look()
    else:
        say("You can't see that")
