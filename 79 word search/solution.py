from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(cords, idx, seen):
            x1, y1 = cords

            if idx == len(path) - 1:
                return True
            found = False
            idx += 1
            for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                x = x + x1
                y = y1 + y
                if (
                    0 <= x < len(board)
                    and 0 <= y < len(board[0])
                    and (x, y) not in seen
                    and board[x][y] == word[idx]
                ):
                    seen.add((x, y))
                    found = found or dfs((x, y), idx, seen)
                    seen.remove((x, y))
            return found

        path = list(word)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == path[0]:
                    seen = {(r, c)}
                    if dfs((r, c), 0, seen):
                        return True
        return False


sol = Solution()


def tests():
    boards = [
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]],
    ]
    words = ["ABCCED", "SEE", "ABCB", "ABCESEEEFS"]
    ans = [True, True, False, True]
    i = 0
    for b, w, a in zip(boards, words, ans):
        i += 1
        res = sol.exist(b, w)
        assert res == a
        print(f"Test {i} passed, output: {res}")


if __name__ == "__main__":
    tests()
