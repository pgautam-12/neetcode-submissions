class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashT = {}
        hashS = {}
        for x in t:
            if x in hashT:
                hashT[x] += 1
            else: 
                hashT[x] = 1
        
        for x in s:
            if x in hashS:
                hashS[x] += 1
            else:
                hashS[x] = 1

        return hashT == hashS