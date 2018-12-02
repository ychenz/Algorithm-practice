# 1. expand and print nested array [1,2,3,4,{2:4},[2,[2,[3]]]] -> [1,2,3,4,{2:4},2,2,3]
# 2. given 2 identical graph, you know root and a leave of the 1st one, and the head of 2nd tree, find the corresponding child of the second tree
def unpack(A):
    result = []
    for i in A:
        if type(i) is list:
            result += unpack(i)
        else:
            result.append(i)
    return result

if __name__ == '__main__':
    A = [1,2,3,4,{2:4},[2,[2,[3]]]]
    print(unpack(A))