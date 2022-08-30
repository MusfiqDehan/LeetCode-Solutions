class Solution:
    def plusOne(self, digits):
        int_list_to_str_list = [str(integer) for integer in digits]
        print(int_list_to_str_list)
        
        a_string = "".join(int_list_to_str_list)
        print(a_string)
        
        an_integer = int(a_string)
        print(an_integer)
        
        # Increment one
        an_integer = an_integer + 1
        print(an_integer)
        
        int_to_int_list = [int(x) for x in str(an_integer)]
        print(int_to_int_list)
        
        return int_to_int_list
    