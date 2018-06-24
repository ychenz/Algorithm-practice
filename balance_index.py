def find_balance_index(A):
    if len(A) < 3:
        return None

    s = sum(A)
    left_sum = 0
    for i in range(0,len(A)-2):
        left_sum += A[i]
        s -= A[i]

        if s - A[i+1] == left_sum:
            return i+1

    return None

if __name__ == '__main__':
    A = [3,0,1,5,1,1,8]
    print(find_balance_index(A))
