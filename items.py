class item():

#Represents an item in the game with a name, description, and damage value.


    def __init__(self, name, description, damage):
        self.name = name
        self.description = description
        self.damage = damage

item1 = item("sword", "a very sharp sword", 50)

class fists():

#Represents a pair of fists that can be used as a weapon in the game.

#The `fists` class represents a pair of fists that can be used to attack enemies. It has a name, description, and damage value that define the properties of the fists.


    def __init__(self, name, description, damage):
        self.name = name
        self.description = description
        self.damage = damage
fists1 = fists("sists", "your fists", 10)

class taser():

#Represents a taser that can be used to stun and electrocute enemies.

#The `taser` class represents a taser weapon that can be used in the game. It has a name, description, and damage value that define the properties of the taser.


    def __init__(self, name, description, damage):
        self.name = name
        self.description = description
        self.damage = damage
taser1 = taser("taser", "a taser that can be used to stun an enemy and electricute them", 20)

class skin():

#Represents a skin item that can be used in the game. A skin provides a certain amount of damage when used as a weapon.

#Args:
    #name (str): The name of the skin.
    #description (str): A description of the skin.
    #damage (int): The amount of damage the skin can inflict.


    def __init__(self, name, description, damage):
        self.name = name
        self.description = description
        self.damage = damage

skin1 = skin("animal skin", "a skin of an animal that heals you", 20)