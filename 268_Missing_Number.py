# 268. Missing Number


def missingNumber(nums: list[int]) -> int:
    result = 0
    for i, num in enumerate(nums):
        result = result ^ i ^ num
    return result ^ len(nums)


def main():
    tests = [[3, 0, 1], [0, 1], [9, 6, 4, 2, 3, 5, 7, 0, 1]]
    for test in tests:
        print(f"{test} = {missingNumber(test)}")


if __name__ == "__main__":
    main()
