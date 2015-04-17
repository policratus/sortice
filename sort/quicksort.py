from utils import rnd, arr


class QuickSort():
    def __init__(self):
        self._array_utils = arr.ArrayUtils()

    def _pivot(self, array):
        # Using median of three method to
        # avoid the chance of choosing a pivot
        # that leads the algorithm to an O(n^2)
        pivot_seeder = rnd.Seeder(len(array), 3)

        pivot_index = pivot_seeder.random_array()

        # Ok, sorry. I used a native Python sort
        # algorithm to find the median.
        pivot_index.sort()

        return pivot_index[len(pivot_index)//2]

    def quick(self, array, left, right):
        if len(array) == 1:
            return array
        elif len(array) > 1:
            pivot = self._pivot(array)

            while left < right:
                while array[left] < array[pivot]:
                    left += 1
                while array[right] > array[pivot]:
                    right -= 1

                if left <= right:
                    print left, right
                    array = self._array_utils.swap(
                        array,
                        left,
                        right
                    )
                    left += 1
                    right -= 1
        self.quick(array, 0, pivot - 1)
        self.quick(array, pivot + 1, len(array) - 1)
