class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        for i in operations:
            if i == '+':
                ans.append(int(ans[-1])+int(ans[-2]))
            elif i == 'C':
                ans.pop()
            elif i == 'D':
                ans.append(2*int(ans[-1]))
            else:
                ans.append(i)
        sum = 0
        for i in ans:
            sum+=int(i)
        return sum


        