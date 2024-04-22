from collections import deque


class Solution:
    def openLock(self, deadends, target: str) -> int:
        target = tuple(int(d) for d in target)
        deadends = set(
            [
                (int(de[0]), int(de[1]), int(de[2]), int(de[3]))
                for de in deadends
            ]
        )
        init = (0, 0, 0, 0)
        que = deque([(init, 0)])
        visited = set([init])

        while len(que) > 0:
            combo, length = que.popleft()

            if combo == target:
                return length   

            if combo not in deadends:
                for i in range(len(combo)):
                    for delta in [-1, 1]:
                        new_combo = list(combo)
                        new_combo[i] = (new_combo[i] + delta) % 10
                        new_combo = tuple(new_combo)

                        if (
                            new_combo not in visited
                            and new_combo not in deadends
                        ):
                            visited.add(new_combo)
                            que.append((new_combo, length + 1))

        return -1