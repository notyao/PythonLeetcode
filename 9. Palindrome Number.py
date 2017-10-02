class Solution(object):
  def isPalindrome(self, x):
      """
      :type x: int
      :rtype: bool
      """
      if x < 0:
          return False
      digits = 1
      while x/digits >= 10:
          digits *= 10
      while digits > 1:
          left = x/digits
          right = x % 10
          if left != right:
              return False
          x = (x%digits) / 10
          digits /= 100
      return True