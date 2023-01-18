'''
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of
all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.
Example 1:
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.

Example 3:
Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
'''


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            if left_sum == total_sum - left_sum - num:
                return i
            left_sum += num

        return -1

'''
Here's an explanation of how the code works:

    The class has a method called pivotIndex that takes in a parameter called nums which is a list of integers.
    It creates a variable called total_sum that stores the sum of all the elements in the input list.
    It also creates a variable called left_sum that is initialized to 0. This variable will be used to keep track of the
    sum of the elements to the left of the pivot index.
    The code then iterates through each element in the input list using a for loop and the enumerate() function, which
    gives us both the index and value of each element.
    For each iteration, it checks if the left_sum is equal to total_sum - left_sum - num, which means that the sum of 
    the elements to the left of the current index is equal to the sum of the elements to the right. If this is true,
    the current index is the pivot index and the method returns it.
    After iterating through all the elements, if no pivot index is found, the method returns -1.
'''