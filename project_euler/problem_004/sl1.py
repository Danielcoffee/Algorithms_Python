def palindromic(n: int) -> int:
    max_num = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            str_ij = str(i*j)
            if str_ij == str_ij[::-1] and i*j < n:
                max_num = max(max_num, i*j)
    return max_num

print(palindromic(30000))
