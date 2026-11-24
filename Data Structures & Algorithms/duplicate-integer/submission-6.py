class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = set() #set doesnt allow duplicates 
        for ele in nums:
            if ele not in dup:
                dup.add(ele)
            else:
                return True
        return False