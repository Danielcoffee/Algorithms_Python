def solution(n: int=1000) -> int:
    multi_3 = []
    multi_5 = []
    temp = 1
    while True:
        result = temp * 3
        if result < n:
            multi_3.append(result)
            temp += 1
        else:
            temp = 1
            break

    while True:
        result = temp * 5
        if result < n:
            multi_5.append(result)
            temp += 1
        else:
            break
    return sum(list(set(multi_3 + multi_5)))

if __name__ == "__main__":
    print(f"{solution() = }")

