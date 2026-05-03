class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = {}

        for num in nums:
            if num in a:
                a[num] += 1
            else:
                a[num] = 1
        
        sorted_list = sorted(a, key= a.get, reverse = True)
        return sorted_list[0:k]

        