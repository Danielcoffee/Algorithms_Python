import math

def prime_number(number):
    if 1 < number < 4:
        return True
    if number <= 1 or number % 2 == 0 or number % 3 == 0:
        return False
    if number > 4:
        for i in range(5, int(math.sqrt(number)+1), 6):
            if number % i == 0 or number % (2+i) == 0:
                return False
        return True

def solution(n: int = 6) -> int:
    # 2, 3, 5, 7, 11, 13
    number_th = 1
    number = 2
    while number_th != n:
        number += 1
        if prime_number(number):
            number_th += 1
    return number

if __name__ == "__main__":
    print(f"{solution() = }")
