def longest_substring(s1,s2):
    char_map = [[0]*len(s1) for c in s2 ]
    max = 0
    max_loc = None

    for i in range(0,len(s2)):
        for j in range(0,len(s1)):
            if s1[j] == s2[i] and i > 0 and j > 0:
                char_map[i][j] = char_map[i-1][j-1] + 1
            elif not s1[j] == s2[i]:
                char_map[i][j] = 0
            else:
                char_map[i][j] = 1

            if char_map[i][j] > max:
                max = char_map[i][j]
                max_loc = (i,j)

    if max_loc:
        substring = ""
        i,j = max_loc
        while i >=0 and j >= 0 and char_map[i][j] > 0:
            substring = s1[j] + substring
            i-=1
            j-=1

        return (max, substring)
    else:
        return (0,None)

def longest_subsequence(s1,s2):

    pass

if __name__ == '__main__':
    print(longest_substring("abcdaf","zabcddadsabcda"))