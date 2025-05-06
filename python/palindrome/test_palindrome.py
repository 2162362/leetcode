import pytest
from palindrome import Solution

def testpalindrome():
    s = Solution()
    assert s.isPalindrome(121) == True
    assert s.isPalindrome(-121) == False