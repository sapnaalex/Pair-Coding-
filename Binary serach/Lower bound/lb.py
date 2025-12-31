def lower_bound(arr, x):
    low = 0
    high = len(arr)
    ans = len(arr)

    while low <= high:
        mid = (low+high) // 2

        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
n = int(input())
arr = list(map(int, input().split()))
x = int(input())
print(lower_bound(arr, x))