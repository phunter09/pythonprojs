def binary_sort(lst, ele):
    start = 0
    end = len(lst)-1
    mid = len(lst)//2
    lst = sorted(lst)
    while ele != lst[mid]:
        if ele > lst[mid]:
            start = mid + 1
            mid = (end - mid)//2
        elif ele < lst[mid]:
            end = mid - 1
            mid = (start + mid)//2
    print(mid)

array = [3,4,5,7,8,9,53]

binary_sort(array, 8)
            
