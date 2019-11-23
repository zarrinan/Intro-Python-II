from room import Room
from player import Player
from item import Item

# Declare all the rooms

ROOM = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
                     passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you,
                     falling into the darkness. Ahead to the north, a light
                     flickers in the distance, but there is no way across the
                     chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from
                      west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
                     chamber! Sadly, it has already been completely emptied by
                     earlier adventurers. The only exit is to the south."""),
}


# Link rooms together
ROOM['outside'].n_to = ROOM['foyer']
ROOM['foyer'].s_to = ROOM['outside']
ROOM['foyer'].n_to = ROOM['overlook']
ROOM['foyer'].e_to = ROOM['narrow']
ROOM['overlook'].s_to = ROOM['foyer']
ROOM['narrow'].w_to = ROOM['foyer']
ROOM['narrow'].n_to = ROOM['treasure']
ROOM['treasure'].s_to = ROOM['narrow']

# Adding items to room
ROOM['foyer'].add_item(Item('torch', 'Helps you find the way in dark'))
ROOM['foyer'].add_item(Item('mask', 'Saves you from dust'))
ROOM['overlook'].add_item(Item('binocular', 'See far away objects'))
ROOM['narrow'].add_item(Item('shoes', 'For better grip on narrow ledges'))
ROOM['treasure'].add_item(Item('box', 'Empty gold box'))
ROOM['treasure'].add_item(Item('map', 'Map to next gold hunt adventure'))

#
# Main
#


def validate_user_input(user_input):
    valid_user_inputs = ['n', 's', 'e', 'w', 'q', 'i', 'inventory']

    split_user_input = user_input.split()
    user_input_len = len(split_user_input)

    # Input user_input should be 2 words at most
    if user_input_len != 1 and user_input_len != 2:
        return False

    if user_input_len == 1:
        if split_user_input[0] not in valid_user_inputs:
            return False

    if user_input_len == 2:
        # Input user_input should be take or drop
        if split_user_input[0] != 'take' and split_user_input[0] != 'drop':
            return False

    return True


def process_user_input(user_input, user):
    split_user_input = user_input.split()
    user_input_len = len(split_user_input)

    if user_input_len == 1:

        if split_user_input[0] == 'q':
            print('\nNice game. Visit again.')
            exit()
        elif split_user_input[0] == 'i' or split_user_input[0] == 'inventory':
            user.print_items_info()
        else:
            if user.move_in_dir(user_input.lower()):
                user.print_room_info()
            else:
                print('\nMoving in this direction is not allowed.')
    else:
        if split_user_input[0] == 'take':
            if user.take_item(split_user_input[1]):
                print(f'\nYou have taken {split_user_input[1]}')
                print(f'\n{user.get_current_room().available_items()}')
            else:
                print('\nItem mentioned not available in room.')
                print(f'\n{user.get_current_room().available_items()}')
        else:
            if user.drop_item(split_user_input[1]):
                print(f'\nYou have dropped {split_user_input[1]}')
            else:
                print('\nItem mentioned not available with you.')


def print_error():
    print('Input invalid.\n')
    print('n - Move in North direction')
    print('s - Move in South direction')
    print('e - Move in East direction')
    print('w - Move in West direction')
    print('\nq - For exiting the game')
    print('\nTake item from a room')
    print('take <item_name>')
    print('\nDrop item in room')
    print('drop <item_name>')


# Make a new player object that is currently in the 'outside' room.
player = Player('Zee')
player.set_current_room(ROOM['outside'])
player.print_room_info()

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


while True:

    command = input('\n Please provide your input: ')

    if not validate_user_input(command):
        print_error()
        continue

    process_user_input(command, player)
