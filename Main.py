import Game
import Dir
import Parser

import Confusion
import sys

def exit():
    print ("Goodbye!")
    sys.exit(0)
def look(cmd):
    if len(cmd)==1:
        obj = Game.curRoom
    else:
        for word in cmd:
            obj = Game.findNoun(word)
            if obj:
                break
    Game.look(obj)
    
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

def process(cmd):
    Game.prompt = ""
    if cmd[0] == "qqq":
        return exit()
    elif cmd[0]=="go":
        travel(cmd)
    elif cmd[0]=="look":
        look(cmd)
    elif cmd[0]== "dont":
        Game.say("Okay, not done.")
    elif cmd[0]== "debug":
        print(cmd)
    elif Game.prompt=="":
        Game.say(Confusion.what())

while True:
    process(Parser.parse(input(Game.prompt+"\n==>")))
