from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        answer = []
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            #seconde boucle for car on veut un 4ème composant
            for j in range(i+1, n):
                #j > i+1 pour éviter de s'arreter à la première itération
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                lo, hi = j+1, n-1
                while lo < hi:
                    summation = nums[i] + nums[j] + nums[lo] + nums[hi]
                    if summation == target:
                        answer.append([nums[i], nums[j], nums[lo], nums[hi]])
                        lo +=1
                        hi -=1
                        while lo < hi and nums[lo] == nums[lo-1]:
                            lo +=1
                        while lo < hi and nums[hi] == nums[hi+1]:
                            hi -=1
                    elif summation < target:
                        lo +=1
                    else:
                        hi -=1
        return answer
