from Player import Player
import os


def check_win(first, second):
    """Returns 0 if draw, 1 if first wins, 2 if second wins"""
    space = ['r', 'p', 's']
    f, s = space.index(first), space.index(second)
    return (f - s + 3) % 3


def get_move():
    while True:
        user_move = input('Please enter your move (r, p, s) or q to quit: ')
        if user_move in {'q', 'debug'}:
            return user_move
        for move in user_move:
            if move not in 'rps':
                print('Please enter a valid move.\n\n')
                return get_move()
        return user_move


def main(mem=100):
    name = input('What is your name? --> ')
    filename = 'Samples/' + name + '.txt'
    player = Player(mem)
    # Load or create file for player
    try:
        with open(filename, 'r') as f:
            print(name + "'s data loaded.")
            for line in f:
                for ch in line:
                    player.add_move(ch)
    except FileNotFoundError:
        if not os.path.exists('Samples/'):
            os.mkdir('Samples/')
        with open('Samples/' + name + '.txt', 'w') as f:
            print('Data file created for ' + name)

    player.history = ''

    score = [0, 0]
    user_move = get_move()
    while user_move != 'q':
        if user_move == 'debug':
            print(player.brain)
        else:
            for move in user_move:
                player_move = player.get_move()
                player.add_move(move)
                print('You played ' + move +
                      ' and the AI played ' + player_move)
                win = check_win(move, player_move)
                if win == 0:
                    print('Draw!')
                elif win == 1:
                    print('You win!')
                    score[0] += 1
                elif win == 2:
                    print('You lose!')
                    score[1] += 1
                print('The score is ' + str(score[0]) + ' - ' + str(score[1]))
                print('\n')

            with open('Samples/' + name + '.txt', 'a') as f:
                f.write(user_move)
        user_move = get_move()


if __name__ == '__main__':
    main(int(input('Difficulty? --> ')))
