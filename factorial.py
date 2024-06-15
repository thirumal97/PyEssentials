# factorial(n) = n * (n-1) * (n-2) * ...* 1

# n = 5
# 120

def factorial(n):
    if n < 0:
        return -1
    if n == 0:
        return 1
    return n * factorial(n-1)

#if __name__ == '__main__':
 #   print(factorial(50))

print(factorial(5))