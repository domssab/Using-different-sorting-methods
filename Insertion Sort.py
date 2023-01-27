def InsertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        array[j + 1] = key

data = [7, 19, 24, 11, 17, 29]
InsertionSort(data)
print("Sorted array in ascending order: ")
print(data)