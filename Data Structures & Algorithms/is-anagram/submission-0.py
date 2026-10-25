class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS = {}
        mapT = {}
        for x in s: 
            if x in mapS:
                mapS[x] += 1
            else:
                mapS[x] = 1

        for x in t:
            if x in mapT:
                mapT[x] +=1
            else:
                mapT[x] =1

        return mapS == mapT