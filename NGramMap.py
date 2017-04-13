from collections import Counter


class NGramMap:
    def __init__(self):
        self.map = dict()

    def add(self, before, after):
        try:
            self.map[before].update([after])
        except KeyError:
            self.map.update({before: Counter()})
            self.map[before].update([after])

    def next_most(self, before):
        """Returns the most common answer for a given key.
        Raises KeyError if the pattern does not exist."""
        return self.map[before].most_common(1)[0][0]

    def __str__(self):
        string = ''
        for key in self.map:
            string += str(key) + ' -->'
            for value in self.map[key].most_common():
                string += ' ' + str(value)
            string += '\n'
        return string