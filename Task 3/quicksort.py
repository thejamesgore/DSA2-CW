def quicksort(arr, left, right):
    if left < right:
        pivot = arr[right - 1] # Pivot point is not the right most but the second right most element of the array
        i = left - 1

        for j in range(left, right - 1):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i] # we swap the elements in place if they are out of order

        arr[i + 1], arr[right - 1] = arr[right - 1], arr[i + 1]
        pivot_index = i + 1

        quicksort(arr, left, pivot_index - 1) # We send the smaller sub arrays back through function
        quicksort(arr, pivot_index + 1, right)

