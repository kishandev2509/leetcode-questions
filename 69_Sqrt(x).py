# 69. Sqrt(x)


def mySqrt(x: int) -> int:
    if x < 2:
        return 2
    low, high = 0, x
    mid = low
    while low < high:
        mid = low + (high - low) // 2
        if x // mid == mid:
            return mid
        elif x // mid < mid:
            high = mid - 1
        else:
            low = mid + 1
    return low if x // low >= low else low - 1


def main():
    tests = [0, 1, 2, 3, 4, 8, 9, 10, 15, 16, 17, 25]
    for test in tests:
        print(f"{test} = {mySqrt(test)}")


if __name__ == "__main__":
    main()
