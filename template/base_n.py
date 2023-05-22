def base_n(num_10: int, n: int):
    """10進数 -> n進数変換(n<=36)"""
    if num_10 == 0:
        return "0"
    s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while num_10:
        res += s[num_10 % n]
        num_10 //= n
    return res[::-1]
