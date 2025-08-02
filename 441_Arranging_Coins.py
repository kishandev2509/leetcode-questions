# 441. Arranging Coins

import math


def arrangeCoins(n: int) -> int:
    return int(math.sqrt(2 * n + 0.25) - 0.5)


def main():
    tests = [5, 8]
    for test in tests:
        print(f"{test} = {arrangeCoins(test)}")


if __name__ == "__main__":
    main()
