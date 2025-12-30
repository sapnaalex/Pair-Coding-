def insertion_sort(arr, i, n):
   
    if i == n:
        return

    j = i
    
    while j > 0 and arr[j - 1] > arr[j]:
        arr[j - 1], arr[j] = arr[j], arr[j - 1]
        j -= 1

    
    insertion_sort(arr, i + 1, n)




n = int(input())
arr = list(map(int, input().split()))
insertion_sort(arr, 0, n)
print(*arr)