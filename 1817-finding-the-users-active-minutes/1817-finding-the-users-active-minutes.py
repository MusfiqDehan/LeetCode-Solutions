class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        user = {}
        ans = [0]*k

        for id, time in logs:
            if id not in user:
                user[id] = set()

            user[id].add(time)
        

        for k,v in user.items():
            ans[len(v)-1] += 1
        

        return ans