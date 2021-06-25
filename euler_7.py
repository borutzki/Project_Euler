def primes(n):
    """
    First prime is hardcoded, as is the number the search starts with.
    """
    primes = [2]
    current_min = primes[len(primes) - 1] + 1

    """
    Looking for prime on position n, using assumption that the prime number is 
    the number which only divides by itself with modulo = 0.
    """
    while len(primes) < n:

        for i in range(2, current_min):

            if current_min % i == 0:
                break
        else:
            primes.append(current_min)

        # print(primes)
        current_min += 1

    print(primes[n - 1])


primes(10001)
