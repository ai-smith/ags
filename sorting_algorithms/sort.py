def bubble_sort(arr):
    """
    Time complexity:
    
    Worst case - O(n^2)
    Best case - O(n)
    Average case - O(n^2)
    ---------------------
    Stability - Yes
    ---------------------
    Space complexity:
    
    Worst case - O(1)
    Best case - O(1)
    Average case - O(1)
    """
    n = len(arr) # O(1)
    for i in range(n - 1): # O(n - 1)
        swapped = False # O(1)
        for j in range(n - i - 1): # O(n - 1 - i)
            if arr[j] > arr[j + 1]: # O(1)
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # O(1)
                swapped = True # O(1)
        if not swapped: # O(1)
            break # O(1)


def selection_sort(arr):
    """
    Time complexity:
    
    Worst case - O(n^2)
    Best case - O(n^2)
    Average case - O(n^2)
    ---------------------
    Stability - No
    ---------------------
    Space complexity:
    
    Worst case - O(1)
    Best case - O(1)
    Average case - O(1)
    """
    n = len(arr) # O(1)
    for i in range(n - 1): # O(n - 1)
        min_idx = i # O(1)
        for j in range(i + 1, n): # O(n - i - 1)
            if arr[j] < arr[min_idx]: # O(1)
                min_idx = j # O(1)
        arr[i], arr[min_idx] = arr[min_idx], arr[i] # O(1)


def insertion_sort(arr):
    """
    Time complexity:
    
    Worst case - O(n^2)
    Best case - O(n)
    Average case - O(n^2)
    ---------------------
    Stability - Yes
    ---------------------
    Space complexity:
    
    Worst case - O(1)
    Best case - O(1)
    Average case - O(1)
    """
    n = len(arr) # O(1)
    for i in range(n-1): # O(n - 1)
        value = arr[i+1] # O(1)
        while i >= 0 and arr[i] > value: # O(n)
            arr[i+1] = arr[i] # O(1)
            i -= 1 # O(1)
        arr[i+1] = value # O(1)


def shell_sort(arr):
    """
    Time complexity:
    
    Worst case - O(n^2)
    Best case - O(n log n)
    Average case - O(n log n)
    ---------------------
    Stability - Noe
    ---------------------
    Space complexity:
    
    Worst case - O(1)
    Best case - O(1)
    Average case - O(1)
    """
    n = len(arr) # O(1)
    interval = n // 2 # O(1)
    while interval > 0: # O(log n)
        for i in range(interval, n): # O(n)
            temp = arr[i] # O(1)
            while i >= gap and arr[i - gap] > temp: # O(n) in worst case
                arr[i] = arr[i - gap] # O(1)
                i -= gap # O(1)
            arr[i] = temp # O(1)
        gap //= 2 # O(1)
                

def merge_sort(arr):
    """
    Time complexity:
    
    Worst case - O(n log n)
    Best case - O(n log n)
    Average case - O(n log n)
    ---------------------
    Stability - Yes
    ---------------------
    Space complexity:
    
    Worst case - O(n)
    Best case - O(n)
    Average case - O(n)
    """
    n = len(arr) # O(n)
    if n > 1: # O(1)
        m = n // 2 # O(1)
        l = arr[:m] # O(m)
        r = arr[m:] # O(n - m)
        merge_sort(l)
        merge_sort(r)
        merge(arr, l, r) # O(n)


def merge(arr, l, r):
    i = j = k = 0 # O(1)
    while i < len(l) and j < len(r): # O(l + r)
        if l[i] <= r[j]: # O(1)
            arr[k] = l[i] # O(1)
            i += 1 # O(1)
        else: # O(1)
            arr[k] = r[j] # O(1)
            j += 1 # O(1)
        k += 1 # O(1)
    while i < len(l): # O(1)
        arr[k] = l[i] # O(1)
        i += 1 # O(1)
        k += 1 # O(1)
    while j < len(r): # O(r)
        arr[k] = r[j] # O(1)
        j += 1 # O(1)
        k += 1 # O(1)


def quick_sort(arr, low=0, high=None):
    """
    Time complexity:
    
    Worst case - O(n^2)
    Best case - O(n log n)
    Average case - O(n log n)
    ---------------------
    Stability - No
    ---------------------
    Space complexity:
    
    Worst case - O(n)
    Best case - O(log n)
    Average case - O(log n)
    """
    if high == None:
        high = len(arr)
    elif low < high:

        pivot = portition(arr, low, high)

        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
        

def portition(arr, low, high):
    val = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= val:
            (arr[i], arr[j]) = (arr[j], arr[i])
            i = i + 1
    (arr[i], arr[high]) = (arr[high], arr[i])
    return i


def counting_sort(arr):
    """
    Time complexity:
    
    Worst case - O(n + k)
    Best case - O(n + k)
    Average case - O(n + k)
    ---------------------
    Stability - Yes
    ---------------------
    Space complexity:
    
    Worst case - O(n + k)
    Best case - O(n + k)
    Average case - O(n + k)
    """
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    count = [0] * range_of_elements
    output = [0] * len(arr)

    for val in arr:
        count[val - min_val] += 1

    for i in range(1, range_of_elements):
        count[i] += count[i - 1]

    for i in arr:
        output[count[i - min_val] - 1] = i
        count[i - min_val] -= 1

    for i in output:
        arr[i] = output[i]
    

        
def radix_sort(arr):
    """
    Time complexity:
    
    Worst case - O(nk)
    Best case - O(nk)
    Average case - O(nk)
    ---------------------
    Stability - Yes
    ---------------------
    Space complexity:
    
    Worst case - O(n + k)
    Best case - O(n + k)
    Average case - O(n + k)
    """
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_radix(arr, exp)
        exp *= 10
        

def counting_radix(arr, exp):

    size = len(arr)
    count = [0] * 10
    output = [0] * size
    
    for i in arr:
        index = (i // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(size):
        arr[i] = output[i]


def bucket_sort(arr):
    """
    Time complexity:
    
    Worst case - O(n^2)
    Best case - O(n + k)
    Average case - O(n + k)
    ---------------------
    Stability - Yes
    ---------------------
    Space complexity:
    
    Worst case - O(n + k)
    Best case - O(n + k)
    Average case - O(n + k)
    """
    size = len(arr)
    if size == 0:
        return arr
    
    max_val = max(arr)
    min_val = min(arr)

    bucket_range = (max_val - min_val) / size + 1
    buckets = [[] for _ in range(size)]

    for val in arr:
        index = int((val - min_val) / bucket_range)
        buckets[index].append(val)

    for bucket in buckets:
        insertion_sort(bucket)

    result = []

    for bucket in buckets:
        result.extend(bucket)

    for i in range(size):
        arr[i] = result[i]
        
def heap_sort(arr):
    """
    Time complexity:
    
    Worst case - O(n log n)
    Best case - O(n log n)
    Average case - O(n log n)
    ---------------------
    Stability - No
    ---------------------
    Space complexity:
    
    Worst case - O(1)
    Best case - O(1)
    Average case - O(1)
    """
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


def heapify(arr, n, i):
    larger = i
    l = i * 2 + 1
    r = i * 2 + 2

    if l < n and arr[l] > arr[larger]:
        larger = l
    if r < n and arr[r] > arr[larger]:
        larger = r
    if larger != i:
        arr[i], arr[larger] = arr[larger], arr[i]
        heapify(arr, n, larger)


def linear_search(arr, k):
    """
    Time complexity:
    
    Worst case - O(n)
    Best case - O(1)
    Average case - O(n)
    ---------------------
    Space complexity:
    
    Worst case - O(1)
    Best case - O(1)
    Average case - O(1)
    """
    for i, val in enumerate(arr):
        if val == k:
            return i


def binary_search_iter(arr, target):
    """
    Time complexity:
    
    Worst case - O(log n)
    Best case - O(log n)
    Average case - O(log n)
    ---------------------
    Space complexity:
    
    Worst case - O(1)
    Best case - O(1)
    Average case - O(1)
    """
    if high == None:
        high = len(arr) - 1
        low = 0

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1


def binary_search_rec(arr, target, high=None, low=0):
    """
    Time complexity:
    
    Worst case - O(log n)
    Best case - O(log n)
    Average case - O(log n)
    ---------------------
    Space complexity:
    
    Worst case - O(1)
    Best case - O(1)
    Average case - O(1)
    """
    if high == None:
        high = len(arr) - 1

    if low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
            return binary_search_rec(arr, target, high, low)
        else:
            high = mid - 1
            return binary_search_rec(arr, target, high, low)