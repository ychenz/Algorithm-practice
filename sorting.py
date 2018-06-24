import math
def merge_sort(A):
    if len(A) < 2:
        return A
    m = int(len(A)/2)
    left = merge_sort(A[0:m])
    right = merge_sort(A[m:len(A)])
    A = merge(left,right,A)
    return A

def merge(left,right,A):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            A[k] = left[i]
            k += 1
            i += 1
        else:
            A[k] = right[j]
            k += 1
            j += 1
    while i < len(left):
        A[k] = left[i]
        k += 1
        i += 1
    while j < len(right):
        A[k] = right[j]
        k += 1
        j += 1
    return A

def radix_sort(A):
    m = max(A)
    temp = []
    exp = 1
    stack_map = {}
    for i in range(0,10):
        stack_map[i] = []

    while True:
        if m/exp > 1:
            for elem in A:
                stack_map[math.floor(elem/exp) % 10].append(elem)

            A = []
            # take element from stack_map bottom up
            for i in range(0,10):
                for e in stack_map[i]:
                    A.append(e)
                stack_map[i] = []

            print(A)
        else:
            break

        exp *= 10  # going to next digit
    return A

def insertion_sort(A):
    for i in range(1,len(A)):
        key = A[i]
        j = i-1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A

if __name__ == '__main__':
    nums = [2,1,3,2,312,0,0,543,32,0,87,6]
    # res = merge_sort(nums)
    nums = [170,45,75,90,802,24,2,66]
    # res = radix_sort(nums)
    res = insertion_sort(nums)
    print(res)