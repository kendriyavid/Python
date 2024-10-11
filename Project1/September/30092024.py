# class Solution(object):
#     def bagOfTokensScore(self, tokens, power):
#         """
#         :type tokens: List[int]
#         :type power: int
#         :rtype: int
#         """
#         tokens.sort()  # Sort tokens once
#         i = 0
#         j = len(tokens) - 1
#         score = 0
#         maxscore = 0
        
#         # Check if there are no tokens or if power is too low to even start
#         if not tokens or power < tokens[0]:
#             return 0

#         while i <= j:
#             # Face up (if power is sufficient to increase the score)
#             if power >= tokens[i]:
#                 power -= tokens[i]
#                 score += 1
#                 i += 1
#             # Face down (if we can sacrifice 1 score to gain more power)
#             elif score >= 1:
#                 power += tokens[j]
#                 score -= 1
#                 j -= 1
#             else:
#                 break  # If neither condition is met, break the loop
            
#             maxscore = max(maxscore, score)  # Update max score
        
#         return maxscore

# # Example usage
# tokens = [100, 200, 300, 400]
# power = 200
# solution = Solution()
# print(solution.bagOfTokensScore(tokens, power))

# class Solution:
#     def __init__(self,people,limit):
#         self.people = people
#         self.limit = limit
    
#     def Savepeople(self):
#         self.people.sort()
#         minboat = 0
#         i=0
#         j=len(self.people)-1
#         while i<=j:
#             if self.people[i]+self.people[j]<=self.limit:
#                 minboat+=1
#                 i+=1
#                 j-=1
#             else:
#                 minboat+=1
#                 j-=1
#         return minboat


# class Solution:
#     def __init__(self,palindrome):
#         self.palindrome = palindrome
    
#     def breakThePal(self):
#         lp = list(self.palindrome)
#         for i in range(len(lp)):
#             if lp[i]=="a":
#                 continue
#             else:
#                 lp[i]="a"
#                 return ''.join(lp)
#         return ""

# palindrome = "aaaa"
# solution = Solution(palindrome)
# print(solution.breakThePal())


class Solution:
    def __init__(self,stvalue,target):
        self.stvalue = stvalue
        self.target = target
    
    def brokenCalculator(self):
        steps = 0
        while self.stvalue!=self.target:
            print(self.stvalue)
            if self.target%2!=0 and self.target//2>self.stvalue:
                self.stvalue = 2*self.stvalue
            else:
                self.stvalue-=1
            steps+=1
        return steps
stvalue = 3
target = 10
solution = Solution(stvalue,target)
print(solution.brokenCalculator())