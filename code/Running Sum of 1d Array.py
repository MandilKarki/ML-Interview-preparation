'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
'''


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        current_sum = 0

        for num in nums:
            current_sum += num
            running_sum.append(current_sum)

        return running_sum

'''
Here's an explanation of how the code works:

    The class has a method called runningSum that takes in a parameter called nums which is a list of integers.
    It creates an empty list called running_sum that will be used to store the running sum of the elements in the input 
    list.
    It also creates a variable called current_sum that is initialized to 0.
    The code then iterates through each element in the input list using a for loop.
    For each iteration, it adds the current element to the current_sum variable and appends the current_sum variable to 
    the running_sum list.
    After iterating through all the elements, it returns the running_sum list.
    The runningSum method returns the list of running sum of the elements in the input list.
    '''