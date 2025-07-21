def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i, j, k = m-1, n-1, m+n-1
    while j >= 0:
        if i>=0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -=1
        else:
            nums1[k] = nums2[j]
            j-=1
        k -=1
        
def main():
    tests = [
        {"nums1": [4, 0, 0, 0, 0, 0], "m": 1, "nums2": [1, 2, 3, 5, 6], "n": 5},
        {"nums1": [4, 5, 6, 0, 0, 0], "m": 3, "nums2": [1, 2, 3], "n": 3},
        {"nums1": [1, 2, 3, 0, 0, 0], "m": 3, "nums2": [2, 5, 6], "n": 3},
        {"nums1": [1, 2, 0], "m": 2, "nums2": [1], "n": 1},
        {"nums1": [1], "m": 1, "nums2": [], "n": 0},
        {"nums1": [0], "m": 0, "nums2": [1], "n": 1},
    ]
    for test in tests:
        merge(nums1=test["nums1"], m=test["m"], nums2=test["nums2"], n=test["n"])
        print(test["nums1"])


if __name__ == "__main__":
    main()
