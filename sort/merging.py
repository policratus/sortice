import numpy as np


class MergeSorting():
    def _to_np_array(self, alist):
        return np.array(alist, dtype=np.uint32)

    def merge(self, array):
        array = self._to_np_array(array)

        if len(array) == 0:
            print "Input array is empty"
        elif len(array) == 1:
            return array
        elif len(array) > 1:
            middle = len(array)//2

            left_half = array[:middle]
            right_half = array[middle:]

            print "Left Half: " + np.array2string(left_half)
            print "Right Half: " + np.array2string(right_half)

            self.merge(left_half)
            self.merge(right_half)
