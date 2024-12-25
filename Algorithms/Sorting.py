def Selection(Data):
    print("Strat Selection Sorting")
    for i in range(len(Data)):
        min_index = i 
        for j in range(i+1 , len(Data)):
            if Data[min_index] > Data[j]:
                min_index = j
        Data[i], Data[min_index] = Data[min_index], Data[i]
        print(f"After pass {i}: the array is = {Data}")
    print("")

def bubble_sort(Data):
    print("Strat Bubble Sorting")
    for i in range(len(Data)):
        for j in range(0, len(Data) - i - 1):
            if Data[j] > Data[j + 1]:
                Data[j], Data[j + 1] = Data[j + 1], Data[j]
        print(f"After pass {i + 1}: the array is = {Data}")
    print("")

def insertion_sort(Data):
    print("Strat Insertion Sorting")
    for i in range(1, len(Data)):
        key = Data[i]
        j = i - 1
        while j >= 0 and key < Data[j]:
            Data[j + 1] = Data[j]
            j -= 1
        Data[j + 1] = key
        print(f"After pass {i}: the array is =  {Data}")
    print("")

# def merge_sort(arr, s, e):
#     if e - s + 1 <= 1:
#         return arr
#     # The middle index of the array
#     m = (s + e) // 2
#     # Sort the left half
#     merge_sort(arr, s, m)
#     # Sort the right half
#     merge_sort(arr, m + 1, e)
#     # Merge sorted halves
#     merge(arr, s, m, e)
#     print(f"After merging ({s}, {m}, {e}): {arr}")
#     return arr

# def merge(arr, s, m, e):
#     # Copy the sorted left & right halves to temp arrays
#     L = arr[s: m + 1]
#     R = arr[m + 1: e + 1]
#     i = 0 # index for L
#     j = 0 # index for R
#     k = s # index for arr
#     # Merge the two sorted halves into the original array
#     while i < len(L) and j < len(R):
#         if L[i] <= R[j]:
#             arr[k] = L[i]
#             i += 1
#         else:
#             arr[k] = R[j]
#             j += 1
#         k += 1
#     # One of the halves will have elements remaining
#     while i < len(L):
#         arr[k] = L[i]
#         i += 1
#         k += 1
#     while j < len(R):
#         arr[k] = R[j]
#         j += 1
#         k += 1

Data = [77,33,44,11,88,22,66,55]
Selection(Data)
bubble_sort(Data)
insertion_sort(Data)
# merge_sort(Data, 0, len(Data) - 1)