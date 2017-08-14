from Room import *
from Item import Item
import Dir
inventory = []
curRoom = None
prompt = None
result = -1
cmd = [""]
caret = "==>"
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

def put(obj1, obj2):
    Game.result = 0
    if not obj1.getable:
        Game.say("You can't get rid of that")
    elif not obj2.locked:
        Game.result = 1
        obj2.inventory.append(obj1)
        Game.inventory.remove(obj1)
    Game.say(obj2.put(obj1))
    Game.cmd = ["put",obj1,obj2]
    print("boba")
    
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
        Game.result = 1
    else:
        Game.say("you can't go that way")
def look(obj):
    if obj:
       obj.look()
    else:
        say("You can't see that")
