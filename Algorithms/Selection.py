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

Data = [77,33,44,11,88,22,66,55]
print(f"{Data}")
Selection(Data)
