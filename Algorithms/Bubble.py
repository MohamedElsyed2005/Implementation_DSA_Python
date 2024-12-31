def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
        print(f"After pass {i}: the array is = {Data}")
    print("")

Data = [77,33,44,11,88,22,66,55]
bubble_sort(Data)