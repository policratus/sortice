import numpy as np


class Seeder():
    def __init__(self, size, seed):
        seed = np.uint8(seed)
        self._random_array = np.random.random_integers(0, seed, size)

    def random_array(self):
        return self._random_array
