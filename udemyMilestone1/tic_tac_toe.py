def win_condition_horizontal(pos):
    checker = check_horizontal((int(pos[0]), int(pos[1])))
    print(checker)
    for tpl in checker:
        print(tpl)
        # if (any(tpl in i for i in WAYS_TO_WIN_HORIZONTAL) and
        #         (not list0.__contains__(' ') and list0 == (['X', 'X', 'X']))
        #         or (not list1.__contains__(' ') and list1.__contains__('X'))
        #         or (not list2.__contains__(' ') and list2.__contains__('X'))):
        #     return True
        # if any(tpl in i for i in WAYS_TO_WIN_HORIZONTAL) and \
        #         (not list0.__contains__(' ') and list0.__contains__('O' * 3)) \
        #         or (not list1.__contains__(' ') and list1.__contains__('O' * 3)) \
        #         or (not list2.__contains__(' ') and list2.__contains__('O' * 3)):
        #     return True
        if any(tpl in i for i in WAYS_TO_WIN_HORIZONTAL) and list0[tpl[0]] == 'X' and \
                list1[tpl[0]] == 'X' and \
                list2[tpl[0]] == 'X':
            return True


# def win_condition_vertical(pos):
#     checker = check_horizontal((int(pos[0]), int(pos[1])))
#     for tpl in checker:
#         if (any(tpl in i for i in WAYS_TO_WIN_HORIZONTAL) and
#         (list0.__contains__('X') and list1.__contains__('X') and list2.__contains__('X')) and
#             not (list0.__contains__(' ') or list0.__contains__(' ') or )


def check_horizontal(pos):
    x = int(pos[0])
    y = int(pos[1])
    if x == 0:
        return (x, y), (x + 1, y), (x + 2, y)
    if x == 1:
        return (x - 1, y), (x, y), (x + 1, y)
    if x == 2:
        return (x - 2, y), (x - 1, y), (x, y)


def check_vertical(pos):
    x = int(pos[0])
    y = int(pos[1])
    if y == 0:
        return (x, y), (x, y + 1), (x, y + 2)
    if y == 1:
        return (x, y - 1), (x, y), (x, y + 1)
    if y == 3:
        return (x, y - 2), (x, y - 1), (x, y)


def initialize_grid(lst0: list, lst1: list, lst2: list, pos=(None, None), symbol=None):
    x = int(pos[0])
    y = int(pos[1])
    if x == 0 and lst0[y] == ' ':
        lst0.pop(y)
        lst0.insert(y, symbol)
    if x == 1 and lst1[y] == ' ':
        lst1.pop(y)
        lst1.insert(y, symbol)
    if x == 2 and lst2[y] == ' ':
        lst2.pop(y)
        lst2.insert(y, symbol)
    draw_grid(lst0, lst1, lst2)


def draw_grid(lst0, lst1, lst2):
    print(lst0)
    print(lst1)
    print(lst2)


def play_game():
    count = 0
    while True:
        if count % 2 == 0:
            print('\nPlayer 1 turn: ')
            input_pos = tuple(
                (input('Enter coordinates of where you want to play, eg 00! Top left corner cell is 00: \n')))
            initialize_grid(list0, list1, list2, input_pos, 'X')
            print('\n')
            count += 1
            if win_condition_horizontal(input_pos):
                print('PLAYER 1 WINS!!')
                break
            elif count == 9:
                print('IT IS A TIE!')
                break
        else:
            print('\nPlayer 2 turn: ')
            input_pos = tuple(
                input('Enter coordinates of where you want to play, eg 00! Top left corner cell is 00: \n'))
            initialize_grid(list0, list1, list2, input_pos, 'O')
            print('\n')
            count += 1
            if win_condition_horizontal(input_pos):
                print('PLAYER 2 WINS!!')
                break
            elif count == 9:
                print('IT IS A TIE!')
                break


if __name__ == '__main__':
    list0 = [' ', ' ', ' ']
    list1 = [' ', ' ', ' ']
    list2 = [' ', ' ', ' ']

    WAYS_TO_WIN_HORIZONTAL = (((0, 0), (0, 1), (0, 2)),
                              ((1, 0), (1, 1), (1, 2)),
                              ((2, 0), (2, 1), (2, 2)))

    WAYS_TO_WIN_VERTICAL = (((0, 0), (1, 0), (2, 0)),
                            ((0, 1), (1, 1), (2, 1)),
                            ((0, 2), (1, 2), (2, 2)))

    play_game()
