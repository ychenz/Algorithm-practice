# Complete the braces function below.
def braces(values):
    result = []

    for value in values:
        stack = []
        done = False

        for char in value:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif len(stack) == 0:
                result.append("NO")
                done = True
                break
            else:
                if char == ')' and stack.pop() == '(':
                    continue
                elif char == ']' and stack.pop() == '[':
                    continue
                elif char == '}' and stack.pop() == '{':
                    continue
                else:
                    result.append("NO")
                    done = True
                    break

        if not done:
            if len(stack) == 0:
                result.append('YES')
            else:
                result.append('NO')

    return result

if __name__ == '__main__':

    values = ['}][}}(}][))]','[](){()}','()','({}([][]))[]()','{)[](}]}]}))}(())(','([[)']
    # values = ['}][}}(}][))]']

    res = braces(values)

    print(res)