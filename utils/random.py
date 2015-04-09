import numpy as np


class Seeder():
    def __init__(self, size):
        self._random_array = np.random.random_integers(0, 2**50, size)

    def random_array(self):
        return self._random_array
