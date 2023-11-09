class ValidParenthesis:
    @staticmethod
    def validParenthesis(str1):
        stack = []

        for char in str1:
            if char in ['(', '{', '[']:
                stack.append(char)
            elif char in [')', '}', ']']:
                if not stack or stack.pop() != char:
                    return False

        return not stack
