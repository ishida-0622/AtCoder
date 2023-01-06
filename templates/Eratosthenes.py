def Eratosthenes(N: int):
    """エラトステネスの篩"""
    is_prime = [True if i % 2 else False for i in range(N+1)]
    is_prime[1], is_prime[2] = False, True

    for p in range(3, N+1, 2):
        if not is_prime[p]:
            continue
        q = p * 2
        while q <= N:
            is_prime[q] = False
            q += p

    return is_prime
