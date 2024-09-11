
from wordle import playWordle
from items import taser1
from items import fists1
from items import item1
class Character:

#Represents a character in the game.

#Args:
    #name (str): The name of the character.
    #health (int): The initial health of the character.

    def __init__(self, name, health):
        self.name = name
        self.health = health

NPC = Character("Diddy", 100)
Player = Character("", 100)
Dragon = Character("Dragon", 100)



def talk_to_player():

    #Handles the player's interaction with the NPC Diddy, including being offered a drink that is tampered with, causing the player to pass out.
    
    Player.name = input("What is your name?")
    print(NPC.name + " says: "+ Player.name +" , welcome to the Celestial Jungle! Here is a cold drink for your travels.")
    print(Player.name + " drinks the cold drink and feels refreshed. Until "+ Player.name+ " passes out. "+ NPC.name +" tampered with the drink.")

def kidnap():

    #Handles the player's escape from a locked room in the Celestial Jungle. The player can either pull a string to turn on a light and find useful items, or try to pick the lock on the door to escape the room. Once outside the room, the player is met with a note indicating they have been captured by the Celestial Jungle and will be fed to the Celestial Dragon. The player can then try to open the next door to the north or return to the hallway.

    print("A few hours later, " + Player.name +" wakes up in some bedroom. The room is dark and there is a door to the north. The door is locked. But you feel something dangling from the ceiling. You make out that it is a string.")
    print("What do you do? (type 'pull' or 'leave')")
    if input() == "pull":
        print("You pull the string and a lightbulb turns on. You find a compass, lockpick and you see that the lock isn't a traditional lock. You figure out that it is some sort of wordle game.")
        playWordle()
    else:
        print("You start feeling around for any objects you can find. You find an oddly shaped lock on the door. You feel around and find a lock pick. You successfully pick the lock and escape the room.")
        print("You feel a lock on the door and find a compass and a lock pick on the floor. Do you want to try and break the lock with the rock or try and pick the lock.(type 'break' or 'pick')")
        if input() == "break":
            print("You break the lock and escape the room, but a guard hears you. You must work quickly to espace the building. You are met with a room with a table. The table has a note on it. The note says: 'You have been captured by the Celestial Jungle.You will be fed to our leader, the Celestial Dragon. There is another door to the north. Do you want to go try and open it or go back to the hallway? (type 'north' or 'south')")
        else:
            print("You try to pick the lock and escape the room.You are met with a room with a table. The table has a note on it. The note says: You have been captured by the Celestial Jungle.You will be fed to our leader, the Celestial Dragon. There is another door to the north. Do you want to go try and open it or go back to the hallway? (type 'north' or 'south')")
            if input() == "north":
                print("You walk through the door and find yourself in a room with a table. The table has a note on it. The note says: 'You have been captured by the Celestial Jungle.You will be fed to our leader, the Celestial Dragon. There is another door to the north. Do you want to go try and open it or go back to the hallway? (type 'north' or 'south')")
                if input() == "north":
                    print("The door is locked. You try to pick the lock, but it is too difficult. You go back to the hallway.")
                else:
                    print("You made it outside! You are free to roam the jungle, but be aware of the Celestial Dragon and its Celestial Guardians.")
    print("You made it outside! You are free to roam the jungle, but be aware of the Celestial Dragon and its Celestial Guardians.")

def outside():

    #Handles the player's exploration of the Celestial Jungle, including interacting with the Celestial Dragon and other NPCs.
    
    #The `outside()` function allows the player to explore the jungle, enter a cave, and ultimately confront the Celestial Dragon. The player can acquire various items and use them to defeat the dragon.
        #have sword
    print("You see a cave. Do you want to go inside the cave or explore the jungle? (type 'cave')")
    if input() == "cave":
        print("You walk into the cave. You see treasure chest. You open the chest and find a "+ item1.name+". You take the sword and continue through the cave and find some vines. Do you want to cut the vines or go back to the jungle. (type 'cut' or 'leave')")
        if input() == "cut":
            print("You cut the vines and continue through the cave and find the Celestial Dragon. You fight the Celestrial Dragon which has " + str(Dragon.health) +" health with your "+ item1.name +" which does " + str(item1.damage) +" damage. You take the first shot but miss. The Celestial Dragon hits you back.")
            Player.health =  (Player.health - 50)
            print("You have " + str(Player.health) + " health left.")
            print("You try to hit the Celestial Dragon and you land a hit. The Celestial Dragon is seriously hurt.")
            Dragon.health =  (Dragon.health - 50)
            print("The dragon has " + str(Dragon.health) + " health left.")
            print("You can either try and jump onto the Dragon and finish it once and for all or try one more basic attack to end it.(type 'jump' or 'attack')")
            if input() == "jump":
                print("You jump onto the Dragon and finish it once and for all. You win the game!")
            else:
                print("You try to hit the Dragon with a basic attack but the Dragon stops you in your tracks and eats you.")
                Player.health =  (Player.health - 50)
                print("The dragon has " + str(Player.health) + " health left.")
                print("You lose the game!")
        else:
            #have sword
            print("You continue exploring the jungle. You an animal that isn't a typical animal you would ever see on Earth. What do you want to do examine it or leave it? (type 'examine' or 'leave')")
            if input() == "examine":
                print("You examine the animal and find that it can heal itself almost instantly about 20 health points. You taser the animal and kill it and pick up its skin which heals you when you eat it. You see a beam of light do you want to go towards the beam of light or go to the cave. (type 'beam' or 'cave')")
                #have skin
                if input() == "beam":
                    print("You walk towards the beam of light and are met with a mountain. You notice there is a cave that seems to go through the mountain. Do you want to go around the mountain or through the cave. (type 'around' or 'cave')") 
                    if input() == "around":
                        print("You walk around the mountain. And ")
                    else:
                        print("You walk over the mountain and get a good viewpoint to see what the beam of light is. You see that it is a Celestial Dragon. You walk towards the dragon and fight it with the weapons you have. You have ")
                else:
                    print("You go into the cave and see vines. Do you want to cut through the vines or go back to the jungle and around the mountain. (type 'cut' or 'around')")
                    if input() == "cut":
                        print("You cut the vines and continue through the cave and find the Celestial Dragon. You fight the Celestrial Dragon which has " + str(Dragon.health) +" health with your "+ item1.name +" which does " + str(item1.damage) +" damage. You take the first shot but miss. After missing you try a jump attack and land an attack on the Celestial Dragon.")
                        Dragon.health =  (Dragon.health - 50)
                        print("The  Celestian Dragon has " + str(Dragon.health) + " health left.")
                        print("With that attack, you made the Celestial Dragon mad at you. He breathes fire at you and you take You have " + str(Player.health) + " health left. Do you want to use your "+ skin1.name +" to heal yourself "+ str(skin1.damage) + " or try to hit the dragon with your "+ item1.name +" again. (type 'heal' or 'attack')")
                        if input() == "heal":
                            print("You use your "+ skin1.name +" to heal yourself "+ skin1.damage + ".")
                            Player.health =  (Player.health + skin1.damage)
                            print("You have " + str(Player.health) + " health left.")
                            print("You try to hit the Celestial Dragon and you land a hit. The Celestial Dragon is seriously hurt and falls to the ground. You win the game!")
                        else:
                            print("You try and attack the dragon but miss. The dragon hits try to hit you back but you dodge it luckily. You notice the dragon is starting to open its mouth to breathe fire at you. Do you want to try and jump attack the dragon again or try and through the "+ item1.name +" into the dragon's mouth and try and stab it that way. (type 'jump' or 'throw')")
                            if input() == "jump":
                                print("You jump onto the Dragon and finish it once and for all. You win the game!")
                            else:
                                print("You throw the "+ item1.name +" into the dragon's mouth, but the dragon eats the "+ item1.name +" and breathes fire at you and you die.")
                        
            else:#have sword
                print("You leave the animal and continue exploring the jungle. You see a beam of light in the distance. You walk towards the light and notice it is on the other side of a mountain. Do you want to go around the mountain or over the mountin? (type 'around' or 'over')")
                if input() == "around":
                    print("You walk around the mountain. And see a guard. Do you want to fight the guard or try and sneak past the guard and continue exploring? (type 'fight' or 'sneak')")
                else:
                    print("You walk over the mountain and get a good viewpoint to see what the beam of light is. You see that it is a Celestial Dragon. You walk towards the dragon and fight it with the weapons you have. You have ")
    else:
        print("You walk back to the Celestial Jungle. You see a Celestial Guard. Do you want to fight the guard or try and sneak past the guard and continue exploring? (type 'fight' or 'sneak')")
        if input() == "fight":
            print("You fight the guard and luckily win without anything but your fists and find some sort of celestial taser. But you have a limited time before the guard must check in. You pick up a taser off of the guard. Do you want to continue exploring the jungle or go into the cave. (type 'cave' or 'jungle')")
            if input() == "cave":
                print("print(You walk into the cave. You see treasure chest. You open the chest and find a "+ item1.name+". You take the sword and continue through the cave and find some vines. Do you want to cut the vines or go back to the jungle. (type 'cut' or 'leave')")
                if input() == "cut":
                    print("You cut the vines and continue through the cave and find the Celestial Dragon. You fight the Celestrial Dragon which has " + str(Dragon.health) +" health with your "+ item1.name +" which does " + str(item1.damage) +" damage. You take the first shot but miss. The Celestial Dragon hits you back.")
                Player.health =  (Player.health - 50)
                print("You have " + str(Player.health) + " health left.")
                print("You try to hit the Celestial Dragon and you land a hit. The Celestial Dragon is seriously hurt.")
                Dragon.health =  (Dragon.health - 50)
                print("The dragon has " + str(Dragon.health) + " health left.")
                print("You can either try and jump onto the Dragon and finish it once and for all or try one more basic attack to end it.(type 'jump' or 'attack')")
                if input() == "jump":
                    print("You jump onto the Dragon and finish it once and for all. You win the game!")
                else:
                    print("You try to hit the Dragon with a basic attack but the Dragon stops you in your tracks and eats you.")
                    Player.health =  (Player.health - 50)
                    print("The dragon has " + str(Player.health) + " health left.")
                    print("You lose the game!")
            else: 
                print("You continue walking through the jungle. You see a beam of light in the distance. You walk towards the light and notice it is on the other side of a mountain. Do you want to go around the mountain or over the mountin? (type 'around' or 'over')")
                if input() == "around":
                    print("You walk around the mountain. And see a guard. Do you want to fight the guard or try and sneak past the guard and continue exploring? (type 'fight' or 'sneak')")
                else:
                    print("As you walk closer to the mountain, you notice there is a cave that seems to go through the mountain. You cut the vines at the end of the cave and are met with the Celestial Dragon.")
                    print("As you begin to start fighting the dragon, you stun it with your taser. The dragon now has ")
                
        else:
            print("You try to sneak past the guard but the guard sees you and you get captured. You have a bag over your head so you don't know where you are going. When the mask is taken off of you, you see the Celestial Dragon. You can't fight back since you are tied down. The Celestial Dragon eats you.")