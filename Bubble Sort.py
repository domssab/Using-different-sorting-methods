def BubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j +1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

data = [7, 19, 24, 11, 17, 29]

BubbleSort(data)

print("Sorted array in ascending order: ")
print(data)

