class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

if __name__ == '__main__':
    x = 121
    print(Solution().isPalindrome(x))