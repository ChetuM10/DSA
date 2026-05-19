# Brute Force approach
class Solution:
    def max_profit(self, prices: list[int]) -> int:

        max_profit = 0
        for buy_day in range(len(prices)):
            for sell_day in range(buy_day + 1, len(prices)):
                profit = prices[sell_day] - prices[buy_day]  # calculate profit

                if profit > max_profit:
                    max_profit = profit  # update max_profit

        return max_profit


prices = list(map(int, input("Enter the Stock prices:").split()))
s = Solution()
print("Maximum Profit is:", s.max_profit(prices))


# Optimal solution
class SolutionOptimized:
    def max_profit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price

            if profit > max_profit:
                max_profit = profit

        return max_profit


prices = list(map(int, input("Enter the Stock prices:").split()))
s = SolutionOptimized()
print("Maximum Profit is:", s.max_profit(prices))
