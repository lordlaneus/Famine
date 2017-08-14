from Game import *
import MainLoop
Game.states={\
    "alterReady": False
    }
Game.prompt = "It's A Cold Day In Hell\n"
bunker = Room("bunker", "A dusty old bunker")
surface = Room("surface", "Everything is dead.")
bedRoom = Room("bedRoom", "Your bedroom is relatively tidy, give the circumstances.")
bunker.addExit(Dir.U,"A rusty ladder leads up","You ascend the ladder to the surface.",surface,)
surface.addExit(Dir.D,"An unremarkable hatch lies beneath you.","You return to your bunker.",bunker) 
surface.addWall(Dir.U,"The sky is obscured by a thick layer of smog.","Try as you might, you fail to break your earthly tether.") 
surface.copyExit(Dir.D,Dir.B)

alter = Item("The Alter", "The dark ritual is almost complete. One ingredient remains.",False, False, "You place @ upon The Alter.")
alter.addAliases("alter")
alter.inText=("displays: ")
skull = Item("A Skull", "The human skull is charred black from the ash.")
skull.addAliases("skull")
bunker.addItem(alter)
surface.addItem(skull)

Game.curRoom = bunker

def process():
    result = Game.result
    cmd = Game.cmd
    if cmd[0]=="put":
        if result == 1 and cmd[1] == skull and cmd[2] == alter:
            Game.say("The Alter hums with a strange power.")
            alter.desc = "The time is now. Activate The Alter, and finish this."
            Game.states["alterReady"] = True
    if cmd[0]=="use":
        print ("using")
        if result == Game.states["alterReady"] and cmd[1] == alter or cmd[2]==alter:
            Game.say("You awake with a start in your bed.")
            Game.curRoom = bedRoom


print(Game.prompt)
while True:
    MainLoop.run()
    process()
    Game.result=-1
    Game.cmd=[""]
    print(Game.prompt)
     




