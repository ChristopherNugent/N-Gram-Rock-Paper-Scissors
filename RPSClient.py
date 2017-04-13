from Player import Player
from os import mkdir

def check_win(first, second):
    """Returns 0 if draw, 1 if first wins, 2 if second wins"""
    space = ['r', 'p', 's']
    f, s = space.index(first), space.index(second)
    return (f - s + 3) % 3


def get_move():
    while True:
        user_move = input('Please enter your move (r, p, s) or q to quit: ')
        if user_move in {'r', 'p', 's', 'q', 'debug'}:
            return user_move
        print('Please enter a valid move.\n\n')


def main(mem=100):
    name = input('What is your name? --> ')
    player = Player(mem)
    try:
        with open('Samples/' + name + '.txt', 'r') as f:
            for line in f:
                for ch in line:
                    player.add_move(ch)
    except FileNotFoundError:
        mkdir('Samples')
        with open('Samples/' + name + '.txt', 'w') as f:
            pass

    score = [0, 0]
    user_move = get_move()
    while user_move != 'q':
        if user_move == 'debug':
            print(player.brain)
        else:
            player_move = player.get_move()
            player.add_move(user_move)
            print('You played ' + user_move +
                  ' and the AI played ' + player_move)
            win = check_win(user_move, player_move)
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
    main()
