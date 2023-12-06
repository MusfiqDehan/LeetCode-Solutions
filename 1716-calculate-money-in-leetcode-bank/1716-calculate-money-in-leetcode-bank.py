class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        extra_days = n % 7
        money = 0
        money += weeks * 28
        money += (7 * weeks * (weeks-1)) // 2

        if extra_days:
            money_to_add = weeks + 1
            for i in range(extra_days):
                money += money_to_add
                money_to_add += 1
                
        return money
        