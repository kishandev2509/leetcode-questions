# 3363. Find the Maximum Number of Fruits Collected
class Solution:
    def maxCollectedFruits(self, fruits: list[list[int]]) -> int:
        n = len(fruits)
        dp = [[-1]*n for _ in range(n)]
        def count_fruits(r, c, m, next_moves):
            if r == c == n-1 :
                return 0
            if r == c or m == 0:
                dp[r][c] = float("-inf")
                return float("-inf")
            if dp[r][c] != -1:
                return dp[r][c]
            max_fruits = -1
            for nm in next_moves:
                nr = r + nm[0]
                nc = c + nm[1]
                if not 0 <= nr < n > nc >= 0:
                    continue
                max_fruits = max(max_fruits,count_fruits(nr,nc,m-1,next_moves))
            if max_fruits == -1:
                dp[r][c] = float("-inf")
                return float("-inf")
            dp[r][c] =  max_fruits + fruits[r][c]
            return max_fruits + fruits[r][c]
        child1 = 0
        for i in range(n):
            child1 = child1 + fruits[i][i]
            
        child2_moves = [(1,-1),(1,0),(1,1)]
        child3_moves = [(-1,1),(0,1),(1,1)]
        
        child2 = count_fruits(0,n-1,n-1,child2_moves)
        dp = [[-1]*(n) for _ in range(n)]
        child3 = count_fruits(n-1,0,n-1,child3_moves)
        
        max_fruits = child1 + child2 + child3
        return int(max_fruits)
        
    


def main():
    tests = [[[1,2,3,4],[5,6,8,7],[9,10,11,12],[13,14,15,16]],[[1,1],[1,1]]]
    for test in tests:
        solution = Solution()
        print(f"{test} = {solution.maxCollectedFruits(test)}")

if __name__ == "__main__":
    main()