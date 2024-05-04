def bubble_sort(arr): #O(n^2)
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                #arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr): #O(n):best , O(n^2):worst
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j 
        temp = arr[min_idx]
        arr[min_idx] = arr[i]
        arr[i] = temp        
        #arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr): #O(n^2):all cases
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

def merge_sort(arr):  #O(nlogn):all cases
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i=j=k=0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Example usage:
arr = [64, 25, 12, 22, 11]
bubble_sort(arr)
print("Bubble Sorted array is:", arr)

arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Selection Sorted array is:", arr)

arr = [64, 25, 12, 22, 11]
insertion_sort(arr)
print("Insertion Sorted array is:", arr)

arr = [64, 25, 12, 22, 11]
merge_sort(arr)
print("Merge Sorted array is:", arr)

arr = [64, 25, 12, 22, 11]
print("Quick Sorted array is:", quick_sort(arr))

#for i in range(0,len(arr)):
   # print(arr[i])
    
#for i in range(0,len(arr)):
    #print(arr[i])    
