from typing import List


def best_time_to_sell_and_buy_stock(prices: List[int]) -> int:
    if not prices:
        return 0
    max_profit = 0
    buy_at = prices[0]

    for i in range(1, len(prices)):
        profit = prices[i] - buy_at
        if profit > max_profit:
            max_profit = profit
        if prices[i] < buy_at:
            buy_at = prices[i]
    return max_profit


print(best_time_to_sell_and_buy_stock([7, 1, 5, 3, 6, 4]))
