class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = {}
        for i in strs:
            b= "".join(sorted(i))
            if b in a:
                a[b].append(i)
            else:
                a[b] = [i]
        return list(a.values())



            
        
        