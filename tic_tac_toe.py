BORDERS, MAX_MOVES = (r'| ', r' |', '-' * 9), 9
RESULT = {'XXX': 'X wins', 'OOO': 'O wins', 0: 'Draw'}

def deck(field):
    print(BORDERS[2])
    [print(' '.join(i).join(BORDERS[:2])) for i in field]
    print(BORDERS[2])

field = [[' ' for _ in range(3)] for _ in range(3)]
lines = ( [(0, 0), (0, 1), (0, 2)],  #
          [(1, 0), (1, 1), (1, 2)],  # horisontals
          [(2, 0), (2, 1), (2, 2)],  #

          [(0, 0), (1, 0), (2, 0)],  #
          [(0, 1), (1, 1), (2, 1)],  # verticals
          [(0, 2), (1, 2), (2, 2)],  #

          [(0, 0), (1, 1), (2, 2)],  #
          [(0, 2), (1, 1), (2, 0)])  # diagonals

deck(field)
moves = MAX_MOVES

while moves:
    while True:
        try:
            x, y = list(map(int, input('Enter the coordinates: ').split()))
            if x <= 0 or y <= 0:
                raise IndexError
            elif not field[x - 1][y - 1] == ' ':
                print('This cell is occupied! Choose another one!')
                continue
            break
        except IndexError:
            print('Coordinates should be from 1 to 3!')
        except ValueError:
            print('You should enter numbers!')
    if moves % 2:
        move = 'X'
    else:
        move = 'O'
    field[x - 1][y - 1] = move
    deck(field)
    moves -= 1

    for line in lines:
        state = ''
        for x, y in line:
            state += field[x][y]
        if RESULT.get(state):
            print(RESULT[state])
            quit()
print(RESULT[moves])