def quick_sort(data):
    if len(data) == 0:
        return data
    
    pivot = data[(len(data) - 1) // 2]
    less = []
    equal = []
    greater = []

    for e in data:
        if e < pivot:
            less.append(e)
        elif e > pivot:
            greater.append(e)
        else:
            equal.append(e)

    return quick_sort(less) + equal + quick_sort(greater)
    
if __name__ == "__main__":
    data = [2, 5, 4, 1, 8, 10, 5, 3, 6, 6, 5, 7, 9, 12, 11]

    data = quick_sort(data)

    print(data)
