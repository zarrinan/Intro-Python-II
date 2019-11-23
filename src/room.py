# Implement a class to hold room information. This should have name and
# Description attributes.
from item import Item
import textwrap


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

        self.items = []

    def __str__(self):
        output = f'{self.name}'

        for desc in textwrap.wrap(self.description):
            output += desc + '\n'

        output += f'Allowed directions {self.allowed_directions()} \n'
        output += f'{self.available_items()} \n'

        return output

    def allowed_directions(self):
        allowed_directions = []
        if self.n_to:
            allowed_directions.append('n')
        if self.s_to:
            allowed_directions.append('s')
        if self.e_to:
            allowed_directions.append('e')
        if self.w_to:
            allowed_directions.append('w')

    def available_items(self):
        room_items_list = self.get_items()
        output = f'{len(room_items_list)} available items in room'
        for item in room_items_list:
            output += f'{item} \n'

        return output

    def add_item(self, item):
        self.items.append(item)

    def get_items(self):
        return self.items

    def remove_item(self, index):
        self.items.pop(index)
