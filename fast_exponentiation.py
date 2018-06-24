def m_pow(x, n):
    if n == 1:
        return x
    elif n % 2 == 0:  # this change the runtime to O(logn)
        y = m_pow(x,n/2)
        return y*y
    else:
        return x*m_pow(x,n-1)

# O(logn)
def mod_m_pow(x,n,m):
    if n == 0:
        return 1
    elif n % 2 == 0:
        temp = mod_m_pow(x,n/2,m)
        return (temp * temp) % m
    else:
        return ((x % m)*mod_m_pow(x, n-1, m)) % m

if __name__ == '__main__':
    print(m_pow(2,300))
    print(mod_m_pow(2,3,5))
    print(mod_m_pow(2,30001,5))