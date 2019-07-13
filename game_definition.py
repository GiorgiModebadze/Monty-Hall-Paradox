import random


def initial_assign():
    choices = ['Goat', 'Goat', 'Car']

    doors = {
        'door_one': '',
        'door_two': '',
        'door_three': ''
    }

    for door in doors:
        random.shuffle(choices)
        doors[door] = choices.pop()

    return doors


def remove_one_goat(doors, chosen_door):
    for door in doors:
        if door != chosen_door:
            if doors[door] == 'Goat':
                del doors[door]
                return doors


def game_play():
    doors = initial_assign()

    chosen_door = random.choice(list(doors))

    doors['chosen_door'] = doors.pop(chosen_door)

    game_result = remove_one_goat(doors, chosen_door)

    for door in game_result:
        if door != 'chosen_door':
            game_result['other_door'] = game_result.pop(door)

    return game_result
