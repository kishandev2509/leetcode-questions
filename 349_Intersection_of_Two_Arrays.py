# 349. Intersection of Two Arrays


def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    # return list({num for num in nums1 if num in nums2})
    return list(set(nums1) & set(nums2))
    
    


def main():
    tests = [[[1,2,2,1],[2,2]],[[4,9,5],[9,4,9,8,4]]]
    for test in tests:
        print(f"{test} = {intersection(test[0],test[1])}")

if __name__ == "__main__":
    main()