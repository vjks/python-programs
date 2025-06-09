class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing_parenthesis = [')', ']', '}']
        matching_brackets = {"(" : ")", "{" : "}", "[" : "]"}
        error = False
        if(len(s) % 2 != 0):
            return False
        for x in s:
            stack.append(x)
            if x in closing_parenthesis:                
                removed = stack.pop()
                if len(stack) < 1:
                    return False
                else:
                    previous = stack.pop()
                if (previous, removed) not in matching_brackets.items():
                    return False
        if stack:
            return False
        else:
            return True
