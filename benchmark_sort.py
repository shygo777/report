import random
import time
import heapq


def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
    return a


def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def heap_sort(a):
    h = list(a)
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]


algos = [
    ('Bubble Sort', bubble_sort),
    ('Selection Sort', selection_sort),
    ('Insertion Sort', insertion_sort),
    ('Merge Sort', merge_sort),
    ('Heap Sort', heap_sort),
]

sizes = [100, 500, 1000, 2000]
print('n,' + ','.join(name for name, _ in algos))
for n in sizes:
    row = [str(n)]
    arr = [random.randint(0, 1000000) for _ in range(n)]
    for _, fn in algos:
        total = 0.0
        for _ in range(3):
            data = list(arr)
            t0 = time.perf_counter()
            fn(data)
            t1 = time.perf_counter()
            total += (t1 - t0)
        row.append(f'{total/3:.6f}')
    print(','.join(row))
