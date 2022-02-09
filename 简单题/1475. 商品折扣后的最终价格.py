def finalPrices(prices: [int]) -> [int]:
    n = prices.__len__()
    lowest_price = prices[-1]
    low_prices = [lowest_price]
    for i in range(n - 2, -1, -1):
        price = prices[i]
        if price >= lowest_price:
            for low_price in low_prices:
                if low_price <= price:
                    prices[i] -= low_price
                    break
            low_prices.insert(0, price)
        else:
            lowest_price = price
            low_prices = [price]
    return prices


if __name__ == '__main__':
    print(finalPrices([8, 4, 6, 2, 3]))
    print(finalPrices([1, 2, 3, 4, 5]))
    print(finalPrices([10, 1, 1, 6]))
