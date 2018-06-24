def test(A):
    m = int(len(A)/2)
    A1 = A[m:len(A)]

    print(A)
    print(A1)
    print("\n")
    A[m] = 0

    print(A)
    print(A1)


if __name__ == '__main__':
    nums = [2,1,3,2,312,543,32,0,87,6]
    test(nums)
