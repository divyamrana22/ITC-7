def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

# Input the number of students
n = int(input("Enter the number of students: "))

# Create an empty list to store the marks
marks = []

# Input the marks for each student
for i in range(n):
    mark = int(input("Enter the mark for student {}: ".format(i + 1)))
    marks.append(mark)

# Sort the list of marks using QuickSort
quicksort(marks, 0, len(marks) - 1)

# Print the sorted list
print("List after sorting is:", marks)
