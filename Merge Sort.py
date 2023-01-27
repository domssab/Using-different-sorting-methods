def MergeSort(array):
    if len(array) > 1:

        r = len(array)//2
        L = array[:r]
        M = array[r:]

        MergeSort(L)
        MergeSort(M)

        i = j = k = 0

