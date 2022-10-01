def selection_sorting(Array):
    size = len(Array)
    for i in range(size - 1):

        min_index = i

        for j in range(i + 1, size):

            if Array[j] < Array[min_index]:
                min_index = j

        Array[i], Array[min_index] = Array[min_index], Array[i]


Array = [3, 1, 41, 59, 26, 53, 59]
print(Array)
selection_sorting(Array)

print(Array)        