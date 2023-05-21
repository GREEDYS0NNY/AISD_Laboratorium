def binary_search(lst, search_element):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if search_element == lst[mid]:
            return 'Element znaleziono'
        elif search_element > lst[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return 'Nie znaleziono'


print(binary_search(sorted([12, 34, 43, 65, 32, 764, 23, 75]), 764))
