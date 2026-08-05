class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = {}
        for i in nums:
            b = i
            if b in a:
                a[b]+=1
            else:
                a[b]=1
        sort = sorted(a,key=a.get,reverse= True)
        return sort[0:k]


            
                


        