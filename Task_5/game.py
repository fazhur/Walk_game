"""Module with classes and methods for the game"""



class Character:
    """General class to represent any game character"""
    def __init__(self, ch_name: str, ch_description: str) -> None:
        """Gives name and description to a character"""
        self.ch_name = ch_name
        self.ch_description = ch_description

    def set_conversation(self, phrase: str):
        """Sets a character's replique"""
        self.phrase = phrase

    def talk(self):
        """Prints character's replique"""
        print(self.phrase)

    def describe(self):
        """Prints a character description for user"""
        print(self.ch_name + 'is here!')
        print(self.ch_description)

    def talk(self):
        """Print's a character's replique"""
        print(f'[{self.ch_name} says]: {self.phrase}')


class Friend(Character):
    """Class to represent a friendly character"""
    def __init__(self, ch_name: str, ch_description: str, hint: str) -> None:
        """Default characters parameteres + useful hint"""
        super().__init__(ch_name, ch_description)
        self.hint = hint

    def give_hint(self):
        """Gives a hint to player in certain conditions"""
        print(self.hint)


class Enemy(Character):
    """Class to renpresent an enemy character"""
    def set_weakness(self, weakness):
        """Sets an item using which character can be defeated"""
        self.weakness = weakness

    def fight(self, item):
        if self.weakness == item:
            return True
        return False


class Item:
    """Class to represent useful items in the rooms"""
    def __init__(self, item_name: str) -> None:
        """Gives a name for the item"""
        self.item_name = item_name

    def set_description(self, item_description: str):
        """Gives a description for the item"""
        self.item_description = item_description

    def describe(self):
        """Prints an item description for user"""
        print(f'The [{self.item_name}] is here - {self.item_description}')

    def get_name(self):
        """Returns a name of the item"""
        return self.item_name


class Room:
    """Class for representing a game room"""
    def __init__(self, room_name: str) -> None:
        """Gives name to the room"""
        self.room_name = room_name
        self.character = None
        self.item = None
        self.rooms = {}

    def get_item(self):
        """Returns item in the current room or None if no items"""
        return self.item

    def get_character(self):
        """Returns character in the current room or None if no characters"""
        return self.character

    def set_character(self, character):
        """Puts a character in the room"""
        self.character = character

    def set_item(self, item):
        """Puts an item in the current room"""
        self.item = item

    def set_description(self, description: str):
        """Gives description for the room"""
        self.room_description = description

    def link_room(self, linked_room, direction: str):
        """Links following room with another one"""
        self.room_description += f'\nThe {linked_room.room_name} is {direction}'
        self.rooms[direction] = linked_room


    def get_details(self):
        """Prints details abour the current room"""
        print(self.room_name)
        print('--------------------')
        print(self.room_description)

    def move(self, direction):
        """Moves to another room in given direction"""
        try:
            return self.rooms[direction]
        except KeyError:
            print('No room in this direction!')
            raise Exception('Try to enter existing direction')
