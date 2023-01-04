class Solution:
    def countDigits(self, num: int) -> int:
        # Initialize a count to keep track of the number of digits that divide num
        count = 0

        # Iterate through the digits in the integer
        for digit in str(num):
            # Check if the digit divides num
            if num % int(digit) == 0:
                # If it does, increment the count
                count += 1

        # Return the count
        return count