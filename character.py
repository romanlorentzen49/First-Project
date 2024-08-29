class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.received = False

    def talk_to_player(self,player_name, player_msg):
        if self.received == False:
            print(f"{self.name} says: {Hi {player_name}. I am looking for a star. Do you have one for me?}")
            YN = input("Do you have a star? (Y/N) ")
            if YN == "Y":
        
            else:
            print(f"{self.name} says: {I see. Keeping looking for a star.}")
        
        else:
            print(f"{self.name} says: {I already have what I need. Go away!}")


    def received_item(self):
        self.received = True
        self.append(item)
        print(f"{self.name} says: {Thank you for the {item.name}. I will treasure it forever.}")