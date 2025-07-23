# 3507. Minimum Pair Removal to Sort Array I


def minimumPairRemoval(nums: list[int]) -> int:
        if len(nums) < 2:
            return 0
        operations = 0
        i = 0
        while i < len(nums) - 1:
            if nums[i] <= nums[i + 1]:
                i += 1
            else:
                minimun = j = 0
                summ = nums[j] + nums[j + 1]
                while j + 1 < len(nums):
                    if summ > nums[j] + nums[j + 1]:
                        summ = nums[j] + nums[j + 1]
                        minimun = j
                    j += 1
                nums[minimun] = summ
                nums.pop(minimun + 1)
                operations += 1
                i = 0
        return operations


def main():
    tests = [[1, 1, 4, 4, 2, -4, -1], [2, 2, -1, 3, -2, 2, 1, 1, 1, 0, -1], [5, 2, 3, 1], [1, 2, 2]]
    for test in tests:
        print(f"{test} = {minimumPairRemoval(test)}")


if __name__ == "__main__":
    main()
