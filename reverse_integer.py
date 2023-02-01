# x = -123
# b =  '-' + str(x)[-1:0:-1] if str(x)[0] == '-' else str(x)[::-1]
# print(b)
class Solution:
    def reverse(self, x: int) -> int:
        sign_multiplier = 1
        if x < 0: 
            sign_multiplier = -1
            x = x * sign_multiplier
        result = 0
        min_int_32 = 2 ** 31
        while x > 0:
            result = result * 10 + x % 10
            if result * sign_multiplier <= -min_int_32 or result * sign_multiplier >=min_int_32-1:
                return 0
            x = x // 10
        return sign_multiplier * result


# 
class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0]=="-":
            sign = -1
        else:
            sign = 1
        x = x.lstrip("-")
        x = x.lstrip("+")
        x = x[::-1]
        int_x = int(x) * sign
        if int_x > 2**31-1:
            return 0
        elif int_x < -2**31:
            return 0
        else:
            return int_x