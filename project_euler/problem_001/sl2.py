def sol2(n: int = 1000) -> int:
    total = 0
    terms = (n - 1)//3
    total += terms * (2*3 + (terms-1)*3)//2
    terms = (n-1)//5
    total += terms * (2*5 + (terms-1)*5)//2
    terms = (n-1)//15
    total -= terms * (2*15 + (terms-1)*15)//2
    return total2

    # remember total of A.P
    # Sn = terms * (a1 * (terms -1) * d) // 2
    # terms = (n - 1)//d
    # a1 is the first multiple of d

if __name__ == '__main__':
    print(f"{sol2() = }")
