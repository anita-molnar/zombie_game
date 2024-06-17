# Create the Character class

class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe the character
    def describe(self):
        print(f"{self.name} is here!")
        print(self.description)
    # Set what this character will say when talked to

    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to the character
    def talk(self):
        if self.conversation is not None:
            print(f"[{self.name} says]: {self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk to you.")

    # Fight the eenemy
    def fight(self, combat_item):
        print(f"{self.name} does not want to fight you.")
        return True
    
    # character check, autorecognise if an enemy or nots
    def is_enemy(self):
        return isinstance(self, Character) and isinstance(self, Enemy)


class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.char_weakness = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print(f"You fend {self.name} off, using {combat_item}.")
            return True
        else:
            print(f"{self.name} crushes you, puny adventurer!")
            print("the game is OVER")
            quit()
            return False
    
    def talk(self):
        super().talk()
        print("I am your enemy")
