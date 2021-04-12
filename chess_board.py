# create a chess board that get start position and end position
# you should return the shortest way the horse should do to get to the end point.


def move_combinations(name):
    if name == 'knight':
        row_x = [2, 1, -1, -2, -2, -1, 1, 2]
        col_y = [1, 2, 2, 1, -1, -2, -2, -1]
        return row_x, col_y
    else:
        # can add here all kinds of moves
        pass


def optional_positions(start_point, name):
    x_move = start_point[0]
    y_move = start_point[1]

    optinal_move = []

    # possible combination
    row_x, col_y = move_combinations(name)

    x_move_opt = x_move
    y_move_opt = y_move

    for i in range(len(row_x)):
        x_move_opt += row_x[i]
        y_move_opt += col_y[i]
        if x_move_opt < 0 or x_move_opt > 7 or y_move_opt < 0 or y_move_opt > 7:
            pass
        else:
            optinal_move.append((x_move_opt, y_move_opt))
        x_move_opt = x_move
        y_move_opt = y_move

    return optinal_move


def dict_options(target, start_point, name):
    dict = {}
    step_number = 0

    opt_steps = optional_positions(start_point, name)
    entry_key = f'step{step_number}_{start_point[0]}_{start_point[1]}'

    dict[entry_key] = opt_steps

    value = opt_steps
    temp_list = []
    temp_list.append(opt_steps)

    not_found = True
    while not_found:
        step_number += 1

        opt_steps = temp_list
        temp_list = []
        for i in range(len(opt_steps)):
            for y in range(len(opt_steps[i])):
                key_name = f'step{step_number}_{opt_steps[i][y][0]}_{opt_steps[i][y][1]}'
                value = optional_positions(opt_steps[i][y], name)

                temp_list.append(value)
                dict[key_name] = value

                if target in value:
                    not_found = False
                    break

            if not_found == False:
                break

    return dict


def shortest_way_to_target(dict, start_point, target):
    final_message = f'Start Point: {start_point[0]},{start_point[1]}\n'
    entry_key = f'step0_{start_point[0]}_{start_point[1]}'

    dict_list = list(dict.items())

    key = dict_list[-1][0]

    string_to_concate = ''

    while key != entry_key:

        previous_step = key.split('_')[0]
        previous_point = key.split('_')[1:]
        string_to_concate += f'{previous_step}: {previous_point[0]},{previous_point[1]}\n-'

        tuple_temp = (int(previous_point[0]), int(previous_point[1]))
        for k, v in dict.items():
            if tuple_temp in v:
                key = k
                break

    for i in reversed(string_to_concate.split('-')):
        final_message += i

    final_message += f'Final Point: {target[0]},{target[1]}!'
    return final_message


def valid_user_input(user_input):
    input_success_step_one = []
    user_input_check = user_input.split(',')
    for num in user_input_check:
        while int(num) > 7 or int(num) < 0:
            print('Error! you should enter only numbers between 0 to 7')
            num = input(f'Please enter a new number instead of {num}: ')

        input_success_step_one.append(int(num))

    return tuple(input_success_step_one)


if __name__ == '__main__':

    print('Hello! to my Chess Game!\nBoard size: 8X8')

    chess_pieces = ['King', 'Queen', 'Bishop', 'Knight', 'Rook', 'Pawn']
    print('\nHere are your choices to play with: ')
    for i in chess_pieces:
        print(i, end=', ')
    user_piece_play = input('\nWould you like to play with Knight or others: ')

    user_start_position = input('Please choose your start position: ')
    user_start_position = valid_user_input(user_start_position)
    user_target_position = input('Please choose your target position: ')
    user_target_position = valid_user_input(user_target_position)

    start_point = user_start_position
    target = user_target_position

    step_options = dict_options(target, start_point, user_piece_play)

    final_msg = shortest_way_to_target(step_options, start_point, target)

    print(final_msg)
