class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.received = False

    def talk_to_player(self,player_name, player_msg):
        print("{self.name} says: {player_name}, welcome to the Celestial Jungle! Here is a cold drink for your travels.")
        print("{player_name} drinks the cold drink and feels refreshed. Until {player_name} passes out. {self.name} tampered with the drink.")

    def kidnap(player_name)
        print("A few hours later, {player_name} wakes up in some bedroom. The room is dark and there is a door to the north. The door is locked. But you feel something dangling from the ceiling. You make out that it is a string.")
        print("What do you do? (type 'pull' or 'leave')")
        if input() == "pull":
            print("You pull the string and a lightbulb turns on. You see a key on the ground. You pick it up and unlock the door. You leave the room.")
        else:
            print("You start feel around for any objects you can find. You find an oddly shaped lock on the door. You feel the lock and feel a puzzle.")