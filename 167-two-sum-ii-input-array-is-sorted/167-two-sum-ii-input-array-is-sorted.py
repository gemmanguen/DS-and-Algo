class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left, right = 0, len(numbers)-1
                
        while left<right: 
        
            tot = numbers[left]+numbers[right]
            if tot == target:
                break
            elif tot < target:
                left += 1
            else:
                right -= 1
        
        return [left+1, right+1]