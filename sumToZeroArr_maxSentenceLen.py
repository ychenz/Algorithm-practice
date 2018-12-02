def solution(N):
    """
    Return an array of N whose sum is 0
    :param N:
    :return:
    """
    sol = []
    half = int(N/2)
    for i in range(1, half + 1):
        sol.append(i)
        sol.append((-1)*i)

    if not N % 2 == 0:
        sol.append(0)
    return sol

def maxWord(S):
    """
    Spliting by !.?, return the max length of sentence, word split by 1 or more spaces
    :param S:
    :return:
    """
    import re
    sentences = filter(None, re.split("[.?!]+", S))
    array_of_length = [len(sentence.split()) for sentence in sentences ]
    return max(array_of_length)

if __name__ == '__main__':
    # N = 100
    # print(solution(N))
    # print(sum(solution(N)))
    S = "We test coders. Give us a try?"
    S = "Forget  CVs..Save time . x x"
    print(maxWord(S))