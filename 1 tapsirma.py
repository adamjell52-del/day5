arr = [64, 34, 25, 12, 22, 11, 90]

bubble = arr.copy()

n = len(bubble)

for i in range(n):
    for j in range(0, n - i - 1):
        if bubble[j] > bubble[j + 1]:
            bubble[j], bubble[j + 1] = bubble[j + 1], bubble[j]

print("Bubble Sort :", bubble)

selection = arr.copy()

for i in range(len(selection)):
    min_index = i

    for j in range(i + 1, len(selection)):
        if selection[j] < selection[min_index]:
            min_index = j

    selection[i], selection[min_index] = selection[min_index], selection[i]

print("Selection Sort :", selection)

python_sort = arr.copy()

python_sort.sort()

print("Python sort() :", python_sort)