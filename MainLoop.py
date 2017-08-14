import Game
import Dir
import Parser
import Confusion
import sys


def exit():
    print ("Goodbye!")
    sys.exit(0)
def drop(cmd):
    unfound = True
    for word in cmd:
        obj = Game.findNoun(word)
        if obj:
            Game.drop(obj)
            unfound = False
            break
    if unfound:
        Game.say("You don't have that")
        Game.result = 0
def get(cmd):
    unfound = True
    for word in cmd:
        obj = Game.findNoun(word)
        if obj:
            Game.pickup(obj)
            unfound = False
            break
    if unfound:
        Game.say("You don't see that")
        Game.result = 0        
def look(cmd):
    if len(cmd)==1:
        obj = Game.curRoom
    else:
        for word in cmd:
            obj = Game.findNoun(word)
            if obj:
                break
    Game.look(obj)

def put(cmd):
    obj1 = None
    obj2 = None
    for word in cmd:
        if not obj1:
            obj1=Game.findNoun(word)
        elif not obj2:
            obj2=Game.findNoun(word)
        else:
            break
    if obj1 and obj2:
        Game.put(obj1,obj2)
    else:
        Game.say("Place what, where?")
        Game.result = 0
        return ["put",obj1,obj2]
      
    
def travel(cmd):
    dir = -1
    for word in cmd:
        dir = Dir.strToDir(word)
        if dir>=0:
            break
    if dir>=0:
        Game.travel(dir)
    else:
        Game.say("Where do you want to go?")
        Game.result=0
def use(cmd):
    obj1 = None
    obj2 = None
    for word in cmd:
        if not obj1:
            obj1=Game.findNoun(word)
        elif not obj2:
            obj2=Game.findNoun(word)
        else:
            break
    if obj1:
        Game.result = 1
        Game.say("You attempt to use " +obj1.name+".")
    else:
        Game.say("use what?")
        Game.result = 0
    Game.cmd = ["use", obj1, obj2]
def process(cmd):
    Game.prompt = ""
    if cmd[0] == "qqq":
        return exit()
    elif cmd[0]=="drop":
        drop(cmd)
    elif cmd[0]=="go":
        travel(cmd)
    elif cmd[0]=="get":
        get(cmd)
    elif cmd[0]=="look":
        look(cmd)
    elif cmd[0]=="put":
        put(cmd)
    elif cmd[0]=="inv":
        Game.showInventory()
    elif cmd[0]=="use":
        use(cmd)
    elif cmd[0]== "dont":
        Game.say("Okay, not done.")
    elif cmd[0]== "debug":
        print(cmd)
def run():
    cmd = Parser.parse(input(Game.caret))
    print()
    process(cmd)
    if Game.prompt=="":
        Game.prompt=Confusion.what()
    return Game.cmd
