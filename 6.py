def remove_duplicates(numbers):
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers

def selection_sort(numbers):
    for i in range(len(numbers)):
        min_index = i
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers

def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n-1):
        for j in range(n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

# Example usage
input_array = [4, 5, 2, 4, 5, 6, 5, 4, 5, 5, 6]
unique_array = remove_duplicates(input_array)
sorted_selection = selection_sort(unique_array)
sorted_bubble = bubble_sort(unique_array)

print("Input array:", input_array)
print("Unique array:", unique_array)
print("Sorted array (Selection sort):", sorted_selection)
print("Sorted array (Bubble sort):", sorted_bubble)
