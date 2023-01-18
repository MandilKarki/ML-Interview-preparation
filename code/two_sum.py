'''
    The class Solution is defined, and within it, the method "twoSum" is defined.
    The method takes in two parameters: a list of integers called "nums" and an integer called "target."
    The method initializes an empty dictionary called "prevMap."
    The method uses a for loop to iterate through the "nums" list, using the enumerate function to keep track of the current
    index, "i," and the current number, "n."
    For each number, "n," in the list, the method calculates the difference between the target and the current
    number: diff = target - n
    The method then checks if the difference, "diff", is in the dictionary "prevMap."
    If "diff" is found in the "prevMap" dictionary, the method returns a list containing the index of the difference
    from the dictionary and the current index.
    If the difference is not found in the dictionary, the current number is added to the dictionary with its index as
    the value.
    After the for loop completes, If the method does not find a match, it will return an empty list.
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

        return
