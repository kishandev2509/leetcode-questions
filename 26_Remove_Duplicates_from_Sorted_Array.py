# 26. Remove Duplicates from Sorted Array

def removeDuplicates(nums: list[int]) -> int:
    i,j = 0,1
    while j < len(nums):
        if nums[i] == nums[j]:
            while nums[i] == nums[j]:
                j+=1
                if j == len(nums):
                    return i+1
            i+=1
            nums[i]=nums[j]
            j+=1
        else:
            i+=1
            nums[i]=nums[j]
            j+=1
    return i+1



def main():
    tests = [[1,1,2,3],[1,2],[1,1],[1,1,2],[0,0,1,1,1,2,2,3,3,4]]
    for test in tests:
        print(f"{test} = {removeDuplicates(test)}, {test}")

if __name__ == "__main__":
    main()