class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result =[]
        keys =[]

        for word in strs:
            key = sorted(word)
            placed = False
            for i in range(len(result)):
                if keys[i] == key:
                    result[i].append(word)
                    placed = True
                    break
            if not placed:
                result.append([word])
                keys.append(key)
        return result


            
        
        