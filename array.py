# Bubble sort start
def bubble_sort(a):
    length = len(a)
    for i in range(length - 1):
        swapped = False
        for j in range(length-1 - i):
            if a[j] > a[j+1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a
# Bubble sort end

# Binary Search start


def binary_search(a, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if a[mid] == x:
            return mid
        elif a[mid] > x:
            return binary_search(a, low, mid-1, x)
        else:
            return binary_search(a, mid + 1, high, x)
    else:
        return -1
# Binary Search end

# Quick sort start


def quick_sort_partition(arr, start, end):
    pivot = arr[start]
    low = start + 1
    high = end
    while True:
        while low <= high and arr[high] >= pivot:
            high = high - 1
        while low <= high and arr[low] <= pivot:
            low = low + 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break
    arr[start], arr[high] = arr[high], arr[start]
    return high


def quick_sort(a, low, high):
    if low < high:
        pi = quick_sort_partition(a, low, high)
        quick_sort(a, low, pi-1)
        quick_sort(a, pi + 1, high)
# Quick sort end

# Merge Sort start


def merge_sort(a):
    if len(a) > 1:
        m = len(a)//2
        L = a[: m]
        R = a[m:]

        merge_sort(L)
        merge_sort(R)
        i, j, k = 0, 0, 0
        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                a[k] = R[j]
                j += 1
            else:
                a[k] = L[i]
                i += 1
            k += 1

        while i < len(L):
            a[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            a[k] = R[j]
            j += 1
            k += 1
# Merge Sort End


# Insertion Sort Start
def insertion_sort(a):
    for i in range(1, len(a)):
        anchor = a[i]
        j = i - 1
        while j >= 0 and anchor < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = anchor
# LINKS https://www.youtube.com/watch?v=K0zTIF3rm9s&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=16
# Insertion Sort End

# Shell Sort Start it is replacement for insertion sort


def shell_sort(a):
    length = len(a)
    gap = length // 2
    while gap > 0:
        for i in range(gap, length):
            anchor = a[i]
            j = i
            while j >= gap and a[j-gap] > anchor:
                a[j] = a[j-gap]
                j -= gap
            a[j] = anchor
        gap = gap // 2
# LINKS https://www.youtube.com/watch?v=VxNr9Vudp4Y&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=18
# Shell Sort End

# Selection Sort Start


def selection_sort(a):
    length = len(a)
    for i in range(length - 1):
        min_index = i
        for j in range(i+1, length):
            if a[j] < a[min_index]:
                min_index = j
        if i != min_index:
            a[i], a[min_index] = a[min_index], a[i]
# LINKS https://www.youtube.com/watch?v=hhkLdjIimlw&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=19

# Selection Sort End


a = [5, 7, 3, 4, 67, 7, 4, 3, 6, 89, 9, 78, 7, 56, 4,
     23, 12, 45, 56, 45, 523234, 6, 345, 56, 345, 45645]
n = len(a)
x = 563
# merge_sort(a)
# quick_sort(a)
# bubble_sort(a)
# insertion_sort(a)
# shell_sort(a)
selection_sort(a)
print(a)
