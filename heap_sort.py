#O(logn)
def min_heapify(A,i):
    left = 2*i
    right = 2*i + 1
    smallest = i
    if left < len(A) + 1 and A[left-1] < A[smallest-1]:
        smallest = left

    if right < len(A) + 1 and A[right-1] < A[smallest-1]:
        smallest = right

    if not smallest == i:
        temp = A[i-1]
        A[i-1] = A[smallest - 1]
        A[smallest - 1] = temp
        min_heapify(A,smallest)
 
# O(n)
def build_heap(A):
    for i in reversed(range(1,int(len(A)/2)+1)):
        min_heapify(A,i)

def remove_min(A):
    r = A[0]
    A[0] = A[-1]
    A = A[:len(A)-1]
    min_heapify(A,0)
    return r,A

#O(nlogn)
def heap_sort(A):
    result = []
    build_heap(A)
    # print(A)
    while len(A) > 1:
        result.append(A[0])  # take min value
        A[0] = A[len(A)-1]
        A = A[0:len(A)-1]
        min_heapify(A,1)
        print(A)

    return result

if __name__ == '__main__':
    nums = [2,1,3,2,312,0,0,543,32,0,87,6]
    build_heap(nums)
    print(nums)
    (r,nums) = remove_min(nums)
    print(nums)
    print(r)

    res = heap_sort(nums)
    print(res)