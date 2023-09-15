import random


def main(mass: list):
    low = 0
    high = len(mass) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_val = mass[mid]
        if mid_val >= 0:
            high = mid - 1
        else:
            low = mid + 1
    count_of_negative = low
    count_of_positive = len(mass) - low
    if count_of_positive > count_of_negative:
        return "положительных больше"
    return "отрицательных больше"


if __name__ == '__main__':
    for _ in range(100):
        array = sorted(random.randint(-100, 100) for el in range(100))
        print(main(array))
