class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        i = 0
        for char in s:
            if char == '(':
                stack.append(('(', i))
            elif char == ')':
                if stack and stack[-1][0] == '(':
                    stack.pop()
                else:
                    stack.append((')', i))
            i += 1
        ans = ''
        i = 0
        wrong_idx = [i[1] for i in stack]
        for char in s:
            if i in wrong_idx:
                i += 1
                continue
            else:
                ans += char
            i += 1
        return ans

assert Solution().minRemoveToMakeValid("())()(((") == "()()"
assert Solution().minRemoveToMakeValid("lee(t(c)o)de)") == "lee(t(c)o)de"
assert Solution().minRemoveToMakeValid("))((") == ""