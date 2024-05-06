def solution(n: int) -> int:
    for i in range(n, 10000, -1):
        str_num = str(i)
        if str_num == str_num[::-1]:
            dividor = 999
            while dividor != 99:
                if i%dividor == 0 and len(str(i//dividor)) == 3:
                    return i
                dividor -= 1

print(solution(1000000))
