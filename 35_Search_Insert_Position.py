# 35. Search Insert Position


def searchInsert(nums: list[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    mid = low
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return low + 1 if nums[low] < target else low


def main():
    tests = [
        [[1, 3, 5, 6], 0],
        [[1, 3, 5, 6], 5],
        [[1, 3, 5, 6], 2],
        [[1, 3, 5, 6], 7],
        [[2, 4, 6, 8], 10],
    ]
    for test in tests:
        print(f"{test} = {searchInsert(test[0], test[1])}")


if __name__ == "__main__":
    main()
