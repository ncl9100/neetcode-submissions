class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = int(tokens[0])
        curr_res = []
        for i in range(0, len(tokens)):
            if tokens[i] == "+":
                x1 = int(curr_res.pop())
                x2 = int(curr_res.pop())
                result = x1 + x2
            elif tokens[i] == "-":
                x1 = int(curr_res.pop())
                x2 = int(curr_res.pop())
                result = x2 - x1
            elif tokens[i] == "*":
                x1 = int(curr_res.pop())
                x2 = int(curr_res.pop())
                result = x1 * x2
            elif tokens[i] == "/":
                x1 = int(curr_res.pop())
                x2 = int(curr_res.pop())
                result = int(x2 / x1)
            else:
                result = int(tokens[i])
            curr_res.append(result)
        return result



        