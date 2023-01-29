class Solution:
    def isPalindrome(self, x: int) -> bool:
            rev = 0
            init_n = x
            if( x < 0):
              return False
            while x != 0:
                    rev = (rev*10) +  x % 10
                    x = x // 10
    
            if(rev == init_n):
                       return True
            return False

# or

class Solution(object):
    def isPalindrome(self, x):
        return True if str(x)==str(x)[::-1] else False