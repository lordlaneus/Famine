from Room import *
from Item import Item
import Dir
map = []
inventory = []
prompt = "It's A Cold Day In Hell"
bunker = Room("bunker", "A dusty old bunker")
surface = Room("surface", "Everything is dead.")

bunker.addExit(Dir.U,"A rusty ladder leads up","You ascend the ladder to the surface.",surface,)
surface.addExit(Dir.D,"An unremarkable hatch lies beneath you.","You return to your bunker.",bunker) 
surface.addWall(Dir.U,"The sky is obscured by a thick layer of smog.","Try as you might, you fail to break your earthly tether.") 
surface.copyExit(Dir.D,Dir.B)

skull = Item("A skull", "The human skull is charred black from the ash.")
skull.addAliases("skull")
surface.addItem(skull)
curRoom = bunker


def drop(obj):
    if obj in Game.inventory:
        if obj.getable:
            inventory.remove(obj)
            curRoom.addItem(obj)
            Game.say("Dropped.")
        else:
            Game.say("You can't drop that.")
    else:
        Game.say("You don't have " +obj.name+".")

    
def findNoun(noun):
    d = Dir.strToDir(noun)
    if d>-1:
        return Game.curRoom.exits[d]
    else:
        for item in curRoom.fullInventory():
            if item.named(noun):
                return item
        for item in inventory:
            if item.named(noun):
                return item
    return None

def pickup(obj):

    if obj in curRoom.fullInventory():
        
        if obj.getable:
            inventory.append(obj)
            curRoom.remove(obj)
            Game.say("Taken.")
        else:
            Game.say("You can't pick up "+obj.name+".")
    elif obj in Game.inventory:
        Game.say ("You already have that.")
    else:
        Game.say("You don't see "+obj.name+".")
def say(s):
    global prompt
    prompt+=s+"\n"

def showInventory():
    global inventory
    if len(inventory)== 0:
        Game.say("Your inventory is empty.")
    else:
        Game.say("Your inventory contains:")
        for item in inventory:
            Game.say(item.name)
    
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
