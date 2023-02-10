class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        store = []

        for i in range(1, n+1):
            ans = ""
            if i % 3 == 0:
                ans += "Fizz"
            if i % 5 == 0:
                ans += "Buzz"
            ans = f"{i}" if ans == "" else ans
            store.append(ans)
        return store
        