# Given an array arr of n elements. The task is to reverse the given array. The reversal of array should be inplace.

class Solution:
    def reverse(self):# i removed arr because i put arr in function if it was outside the dunction i had to add def reverse(self,add):
       arr = list(range(1,6))
       

       reversed_numbers = arr[::-1] # we can also use arr.reverse()
       print(reversed_numbers)
obj = Solution()
obj.reverse()
