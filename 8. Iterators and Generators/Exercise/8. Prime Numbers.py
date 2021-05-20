def get_primes(elements):
    for el in elements:
        if el < 2:
            continue
        is_prime = True
        for i_num in range(2, el):
            if el % i_num == 0:
                is_prime = False
                break
        if is_prime:
            yield el


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))