def rotate_left(S,d):
    l = S[0:d]
    r = S[d:]
    return r+l

def rotate_right(S,d):
    l = S[0:len(S) - d]
    r = S[len(S) - d:]
    return r + l

def asc2_add(S,d):
    r = ""
    for c in S:
        r += chr(ord(c) + d)

    return r

if __name__ == '__main__':
    str = "abcdefg"
    print(rotate_left(str,2))
    print(rotate_right(str,3))
    print(asc2_add(str,3))