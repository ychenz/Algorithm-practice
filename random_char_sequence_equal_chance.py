def generate(id):
    letters = ['a','b','c','d']
    res = ''
    mod = len(letters)
    while len(letters) > 0:
        res += letters[id % mod]
        letters.pop(id % mod)
        id=id/mod
        id = int(id)
        mod -=1
    return res

if __name__ == '__main__':
    map = {}
    # 24 arrangement in total
    for i in range(0,24):
        if generate(i) in map:
            print("WTF")
        else:
            print(generate(i))

        map[generate(i)] = i