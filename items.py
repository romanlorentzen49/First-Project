class item():
    def __init__(self, name, description, damage):
        self.name = name
        self.description = description
        self.damage = damage

item1 = item("sword", "a very sharp sword", 50)

class fists():
    def __init__(self, name, description, damage):
        self.name = name
        self.description = description
        self.damage = damage
fists1 = fists("sists", "your fists", 10)

class taser():
    def __init__(self, name, description, damage):
        self.name = name
        self.description = description
        self.damage = damage
taser1 = taser("taser", "a taser that can be used to stun an enemy and electricute them", 20)

class skin():
    def __init__(self, name, description, damage):
        self.name = name
        self.description = description
        self.damage = damage

skin1 = skin("animal skin", "a skin of an animal that heals you", 20)