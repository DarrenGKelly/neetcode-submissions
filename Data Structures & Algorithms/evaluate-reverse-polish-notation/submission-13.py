class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]

        while (len(tokens) > 0):
            tokenVal = tokens.pop(0)

            if (tokenVal not in operators):
                stack.insert(0, int(tokenVal))
                continue
            else:
                operator = tokenVal

                val1 = stack.pop(0)
                val2 = stack.pop(0)

                if (operator == "+"):
                    stack.insert(0, val2 + val1)
                
                elif (operator == "-"):
                    stack.insert(0, val2 - val1)

                elif (operator == "*"):
                    stack.insert(0, val2 * val1)
                
                elif (operator == "/"):
                    stack.insert(0, int(val2 / val1))

        return stack[0]