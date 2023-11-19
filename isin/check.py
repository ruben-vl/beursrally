with open("isin/funds.txt", "r") as f:
    funds = [x.strip() for x in f.readlines()]

with open("isin/stocks.txt", "r") as f:
    stocks = [x.strip() for x in f.readlines()]

assert len(funds) == len(set(funds))
assert len(stocks) == len(set(stocks))
