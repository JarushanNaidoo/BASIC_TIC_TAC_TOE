def key_mappings(value):
    key = dict()
    if value not in nums:
        print('Input not valid')
    else:
        key['1'] = (0, 0)
        key['2'] = (0, 1)
        key['3'] = (0, 2)
        key['4'] = (1, 0)
        key['5'] = (1, 1)
        key['6'] = (1, 2)
        key['7'] = (2, 0)
        key['8'] = (2, 1)
        key['9'] = (2, 2)
    return key[value]


def play_game(brd):
    count = 0
    while True:
        if count % 2 == 0:
            print('\nPlayer 1 turn: ')
            input_pos = input('Enter the number of the cell you want to pick:\n')
            draw_board(brd, key_mappings(input_pos), 'X')
            count += 1
            if win_condition(brd, key_mappings(input_pos), 'X') and count >= 5:
                print('PLAYER 1 WINS!!')
                break
            elif count == 9:
                print('IT\'S A TIE!!')
                break
        else:
            print('\nPlayer 2 turn: ')
            input_pos = input('Enter the number of the cell you want to pick:\n')
            draw_board(brd, key_mappings(input_pos), 'O')
            print('\n')
            count += 1
            if win_condition(brd, key_mappings(input_pos), 'O') and count >= 5:
                print('PLAYER 2 WINS!!')
                break
            elif count == 9:
                print('IT\'S A TIE!!')
                break


def initialize_board(brd):
    print('--------------')
    for i in range(3):
        print(end='| ')
        for j in range(3):
            print(brd[i][j], end=' | ')
        print('\n--------------')


def draw_board(brd, pos=None, symbol=None):
    x = pos[0]
    y = pos[1]
    if (0, 0) <= (x, y) <= (2, 2):
        if brd[x][y] in nums:
            brd[x].pop(y)
            brd[x].insert(y, symbol)
            initialize_board(brd)
    else:
        raise Exception('Coordinate does not exist')


def win_condition(brd, pos, symbol):
    x = pos[0]
    y = pos[1]
    flag = []
    for i in WAYS_TO_WIN[(x, y)]:
        for j in i:
            if brd[j[0]][j[1]] == symbol:
                flag.append(True)
            else:
                flag.append(False)
    return True if flag[0] == True and flag[1] == True else False


if __name__ == '__main__':
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

    WAYS_TO_WIN = dict()
    # Ways to win, input row 1
    WAYS_TO_WIN[(0, 0)] = [[(0, 1), (0, 2)], [(1, 0), (2, 0)], [(1, 1), (2, 2)]]
    WAYS_TO_WIN[(0, 1)] = [[(0, 0), (0, 2)], [(1, 1), (2, 1)]]
    WAYS_TO_WIN[(0, 2)] = [[(0, 0), (0, 1)], [(1, 2), (2, 2)], [(1, 1), (2, 0)]]

    # Ways to win, input row 2
    WAYS_TO_WIN[(1, 0)] = [[(1, 1), (1, 2)], [(0, 0), (2, 0)]]
    WAYS_TO_WIN[(1, 1)] = [[(0, 0), (2, 2)], [(1, 0), (1, 2)], [(0, 1), (2, 1)], [(0, 2), (2, 0)]]
    WAYS_TO_WIN[(1, 2)] = [[(0, 2), (2, 2)], [(1, 1), (1, 0)]]

    # Ways to win, input row 3
    WAYS_TO_WIN[(2, 0)] = [[(2, 1), (2, 2)], [(1, 0), (0, 0)], [(1, 1), (0, 2)]]
    WAYS_TO_WIN[(2, 1)] = [[(2, 0), (2, 2)], [(1, 1), (0, 1)]]
    WAYS_TO_WIN[(2, 2)] = [[(0, 0), (1, 1)], [(1, 2), (0, 2)], [(2, 1), (2, 0)]]

    initialize_board(board)
    play_game(board)
