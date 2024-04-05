class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and (
                (char.islower() and char.upper() == stack[-1])
                or (char.isupper() and char.lower() == stack[-1])
            ):
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)


assert Solution().makeGood("Pp") == ""
assert Solution().makeGood("leEeetcode") == "leetcode"
