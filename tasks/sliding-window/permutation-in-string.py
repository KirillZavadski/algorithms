from collections import deque, Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        ptr1 = 0
        dick = Counter(s1)
        dick2 = dick.copy()
        queue = deque()
        for i in range(len(s2)):
            if s2[i] in s1:
                dick2[s2[i]] -= 1
                queue.append(s2[i])

                while dick2[s2[i]] < 0:
                    el_queue = queue.popleft()
                    dick2[el_queue] += 1

                if len(queue) == window:
                    return True
            else:
                if len(s2)-i < len(s1):
                    return False
                queue = deque()
                dick2 = dick.copy()
        return False