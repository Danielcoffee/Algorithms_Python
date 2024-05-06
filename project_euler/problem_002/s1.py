def solution(n: int=4000000) -> int:
    fibo_list = []
    a = 1
    b = 2
    while b < n:
        if b % 2 == 0:
            fibo_list.append(b)
        a, b = b, b + a
    return sum(fibo_list)

if __name__ == "__main__":
    print(f"{solution() = }")

