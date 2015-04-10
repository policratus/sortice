import numpy as np


class MergeSort():
    def _to_np_array(self, alist):
        return np.array(alist, dtype=np.uint32)

    def divide(self, array):
        array = self._to_np_array(array)

        if len(array) == 0:
            print "Input array is empty"
        elif len(array) == 1:
            return array
        elif len(array) > 1:
            middle = len(array)//2

            left_half = array[:middle]
            right_half = array[middle:]

            self.merge(left_half)
            self.merge(right_half)

    def merge(self, left_array, right_array):
        result_array = np.array([])
        count_left, count_right = 0, 0

        while (count_left < len(left_array) and count_right < len(right_array)):
            if left_array[count_left] > right_array[count_right]:
                result_array.append
            count_left += 1
            count_right += 1
