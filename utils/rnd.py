import random


class Seeder():
    def __init__(self, limit, size):
        self._random_array = random.sample(xrange(limit), size)

    def random_array(self):
        return self._random_array
