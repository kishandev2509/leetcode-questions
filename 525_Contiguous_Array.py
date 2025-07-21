
def findMaxLengthm(nums: list[int]) -> int:
    i,j,k = 0,0,1
    largest = 0
    while i < k and k < len(nums):
        if nums[j] == nums[i]:
            j+=1
            k=j+1
        else:
            if nums[k] == nums[j]:
                k+=1
            else:
                i=j
        if k-j >j-i:
            j+=1
            i+=1
        largest = max(largest,(k-j))
    return largest*2


def findMaxLength(nums: list[int]) -> int:
    balance = max_length = 0
    balance_map = {0: -1}
    
    for index, value in enumerate(nums):
        balance += 1 if value == 1 else -1
        
        if balance in balance_map:
            max_length = max(max_length, index - balance_map[balance])
        else:
            balance_map[balance] = index
    return max_length


def main():
    tests = [[0,1,1],[0,1],[0,1,0],[0,1,1,1,1,1,0,0,0]]
    for test in tests:
        print(f"{test} = {findMaxLength(test)}")

if __name__ == "__main__":
    main()
    # empty =[]
    # print(empty.pop())
    # print(empty)