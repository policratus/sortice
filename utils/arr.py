class ArrayUtils():
    def swap(self, array, idx_first, idx_second):
        first = array[idx_first]
        second = array[idx_second]

        array[idx_second] = first
        array[idx_first] = second

        return array
