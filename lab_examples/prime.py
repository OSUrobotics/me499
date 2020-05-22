def is_prime(n):

    n = abs(n)
    if n == 1:
        return False

    for divisor in range(2, n):
        if not n % divisor:
            return False
    return True

if __name__ == '__main__':
    print(is_prime(-6))
    print(is_prime(13))

    print(is_prime(6))
    print(is_prime(12))