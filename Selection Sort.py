def slectionSort(array, size):
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):

            if array[i] < array[min_idx]:
                min_idx = i