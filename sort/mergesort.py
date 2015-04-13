class MergeSort():
    def run(self, array):
        # Base Cases
        if len(array) == 0:
            print "Input array is empty"
        elif len(array) == 1:
            return array
        elif len(array) > 1:
            middle = len(array)//2

            left_half = array[:middle]
            right_half = array[middle:]

            # Two recursive calls to split
            # This denotes a recurrence of
            # T(n) = 2*T(n/2) + n
            # Using the second case of
            # master method
            self.run(left_half)
            self.run(right_half)

            count_left, count_right, count_result = 0, 0, 0

            # Merging
            while (count_left < len(left_half)
                   and count_right < len(right_half)):
                if left_half[count_left] < right_half[count_right]:
                    array[count_result] = left_half[count_left]
                    count_left += 1
                else:
                    array[count_result] = right_half[count_right]
                    count_right += 1

                count_result += 1

            while (count_left < len(left_half)):
                array[count_result] = left_half[count_left]
                count_left += 1
                count_result += 1

            while (count_right < len(right_half)):
                array[count_result] = right_half[count_right]
                count_right += 1
                count_result += 1

            return array
