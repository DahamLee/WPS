def binary_search(data, target):
    data.sort()
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid
        elif data[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

if __name__ == "__main__":
    data = [i**2 for i in range(1, 11)]

    target = 1000
    idx = binary_search(data, target)

    if idx == None:
        print("{}이 존재하지 않습니다".format(target))
    else:
        print("찾는 데이터의 인덱스는 {}이고 데이터는 {} 입니다".format(idx, data[idx]))

