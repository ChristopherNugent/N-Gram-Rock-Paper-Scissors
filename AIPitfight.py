from Player import Player
from RPSClient import check_win

def main(games=10, mem1=20, mem2=20):
    score = [0, 0]

    p1 = Player(mem1)
    p2 = Player(mem2)

    for i in range(games):
        m1 = p1.get_move()
        m2 = p2.get_move()
        p1.add_move(m2)
        p2.add_move(m1)
        if check_win(m1, m2) != 0:
            score[check_win(m1, m2) - 1] += 1

    print('The final score is ' + str(score[0]) + ' - ' + str(score[1]))

    with open('AI_Scores.txt', 'w') as f:
        f.write('The final score is ' + str(score[0]) + ' - ' + str(score[1]))
        # print()
        f.write('\n------------------------------------------------------------\n')
        f.write(str(p1.brain))
        f.write('\n------------------------------------------------------------\n')
        f.write(str(p2.brain))


if __name__ == '__main__':
    main(1000, mem2=100)