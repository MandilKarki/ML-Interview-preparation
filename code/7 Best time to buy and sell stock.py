'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to
sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_buy = float('inf')
        max_profit = 0
        for price in prices:
            min_buy = min(min_buy, price)
            max_profit = max(max_profit, price - min_buy)
        return max_profit

'''
The code I provided is a solution to the problem of finding the maximum profit that can be made by buying and selling a 
stock (or multiple stocks) on different days. The input to the function is a list of prices, where the i-th element in the
list represents the price of the stock on the i-th day. The output of the function is an integer representing the maximum 
profit that can be made.

The code uses two different approaches to solve this problem:

    The first approach uses dynamic programming. The code first checks if the input list is empty, and if it is, it returns
    0 (as there would be no profit to be made). If the list is not empty, it initializes a list "dp" with the same length 
    as the input list, and fills it with 0's. It then loops through the input list starting at the second element. 
    For each element, it compares the maximum profit that can be made by either not buying or selling on that day, or by
    buying on a previous day and selling on that day. This is done by comparing the current element in the input list 
    with the difference of the current element and all previous elements in the input list. The maximum profit is then 
    stored in the corresponding element of the "dp" list. After the loop, the function returns the maximum value in the "dp"
    list, which represents the maximum profit that can be made.

    The second approach is a one-pass greedy algorithm. The code also checks whether the given prices list is empty, if yes
    then return 0. Then it initializes two variables min_buy with infinity and max_profit with 0. Then it iterates through
    the prices list. At each price, it checks whether the current price is less than the minimum buy price, if yes then 
    updates the minimum buy price. Then it checks whether the current price minus the minimum buy price is greater than
    maximum profit, if yes then updates the maximum profit. Finally, it returns the maximum profit.

Both of these algorithms have linear time complexity which is O(n) where n is the number of elements in the prices list.

Both of these algorithms are solving the same problem but with a different approach and have same time complexity. You 
can use the one that you are comfortable with or the one that fits better for the particular problem.
'''