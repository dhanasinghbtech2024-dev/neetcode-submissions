class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        si = set(s)
        ti = set(t)
        if len(si) != len(ti):
            return False
        else:
            le = []
            for i in si:
                if s.count(i) == t.count(i):
                    le.append(i)
                else:
                    continue
            if len(le) == len(si):
                return True
            else:
                return False