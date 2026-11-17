class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # only student availability matters
        q = deque(students)
        res = len(sandwiches)
        for s in sandwiches:
            count = 0
            while count < res and q[0] != s:
                curr_student = q.popleft()
                q.append(curr_student)
                count+=1
            if count == res:
                return res
            else:
                q.popleft()

                res-=1
        return res

        