# 350. Intersection of Two Arrays II


def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    counts = {}
    for num in nums1:
        counts[num] = counts[num] + 1 if num in counts else 1
    result = []
    for num in nums2:
        if num in counts and counts[num] > 0:
            result.append(num)
            counts[num] -= 1
    return result


def main():
    tests = [[[1, 2, 2, 1], [2, 2]], [[4, 9, 5], [9, 4, 9, 8, 4]], [[1, 2, 2, 1], [2]]]
    for test in tests:
        print(f"{test} = {intersect(test[0], test[1])}")


if __name__ == "__main__":
    main()
