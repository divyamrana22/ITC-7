def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Input the array containing duplicates
arr = list(map(int, input("Enter the integer array with duplicates (comma-separated): ").split(',')))

# Sort the array
arr.sort()

# Input the element to search
element = int(input("Enter the element to search: "))

# Perform binary search
index = binary_search(arr, element)

# Count the occurrences
count = arr.count(element)

# Print the sorted array
print("Sorted array:", arr)

# Check if the element was found
if index != -1:
    print("Number of occurrences of element", element, "is:", count)
else:
    print("Element", element, "not found in the array.")
