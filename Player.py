from NGramMap import NGramMap
import random


class Player:
    def __init__(self, memory=10):
        self.brain = NGramMap()
        self.history = ''
        self.memory = memory

    def update_history(self, move):
        if len(self.history) < self.memory:
            self.history += move
        else:
            self.history = self.history[1:] + move

    def add_move(self, move):
        for i in range(self.memory):
            self.brain.add(self.history[i:], move)
        self.update_history(move)

    def get_move(self):
        count = 0
        # Keep trying to get value from history, using one less move of history
        # each time
        while count < self.memory and count < len(self.history):
            try:
                counter = self.brain.map[self.history[count:]]
                rand = random.randrange(sum(counter.values()))
                next_move = ''
                for k in counter:
                    rand -= counter[k]
                    if rand < 0:
                        next_move = k
                        break
                space = ['r', 'p', 's']
                response = space[(space.index(next_move) + 1) % 3]
                return response
            except KeyError:
                count += 1

        return random.choice(['r', 'p', 's'])
