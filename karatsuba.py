## recursive integer multiplication / Karatsuba multiplication

a = 3141592653589793238462643383279502884197169399375105820974944592
b = 2718281828459045235360287471352662497757247093699959574966967627

# a = 314159265358979323846264338327950288419716939937510582097494944592
# b = 271828182845904523536028747135266249775724709369995957496696

def karatsuba(x, y):
    # multiply two n-digit integers
    print('multiplying: %s x %s' % (x,y))
    n = int(len(str(x)))
    m = int(len(str(y)))
    if n == 1 and m == 1:
        print('returning: %s' % (x*y))
        return x*y
    a = int(str(x)[:int(n/2)])
    b = int(str(x)[int(n/2):])
    c = int(str(y)[:int(n/2)])
    d = int(str(y)[int(n/2):])
    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    abcd = karatsuba((a+b),(c+d)) - ac - bd
    res = (10^n)*ac + (10^int(n/2))*abcd + bd
    print('returning: %s' % res)
    return res

# print(karatsuba(12, 12))
from math import ceil, floor

# def recursive_int_multiply(x, y):
#     # multiply two n-digit integers, where n is a power of 2
#     print('multiplying: %s x %s' % (x,y))
#     x = str(x)
#     y = str(y)

#     # n = max(int(len(str(x))), int(len(str(y))))
#     if n == 1: return x*y
#     n_2 = int(n/2)
#     a = str(x)[:n_2]
#     b = str(x)[n_2:]
#     c = str(y)[:n_2]
#     d = str(y)[n_2:]
#     assert len(a) == len(b) == len(c) == len(d)
#     a = int(a)
#     b = int(b)
#     c = int(c)
#     d = int(d)
#     # a = int(str(x)[:n_2]) if str(x)[:n_2] != '' else 0
#     # b = int(str(x)[n_2:]) if str(x)[n_2:] != '' else 0
#     # c = int(str(y)[:n_2]) if str(y)[:n_2] != '' else 0
#     # d = int(str(y)[n_2:]) if str(y)[n_2:] != '' else 0
#     ac = recursive_int_multiply(a,c)
#     bd = recursive_int_multiply(b,d)
#     ad = recursive_int_multiply(a,d)
#     bc = recursive_int_multiply(b,c)
#     res = (10**n)*ac + (10**n_2)*(ad+bc) + bd
#     print('returning: %s' % res)
#     return int(res)

def recursive_int_multiply(x, y):
    # multiple two n-digit integers, where n is a power of 2
    print('called with %s x %s' % (x,y))
    if len(str(x)) == 1 or len(str(y)) == 1:
        print('returned base case: %s x %s' % (x,y))
        return x*y
    else:
        n = max(len(str(x)), len(str(y)))
        n_2 = int(n // 2)
        a = int(x // 10**(n_2))
        b = int(x % 10**(n_2))
        c = int(y // 10**(n_2))
        d = int(y % 10**(n_2))
        ac = recursive_int_multiply(a,c)
        bd = recursive_int_multiply(b,d)
        ad = recursive_int_multiply(a,d)
        bc = recursive_int_multiply(b,c)
        res = ac*10**(2*n_2) + (ad+bc)*10**(n_2) + bd
        print('returned %s for: %s x %s' % (res, x,y))
        return int(res)

print(recursive_int_multiply(a, b))