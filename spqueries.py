import csv

with open("/constituents-financials_csv.csv") as csvfile:
    const = csv.reader(csvfile, delimiter=",")

    # for row in const:
    #     print(', '.join(row))

    for row in const:
        print("INSERT INTO sp500 (symbol, name, sector, price, price_per_earnings, "
              "dividend_yield, earnings_per_share, 52_week_low, 52_week_high, market_cap, "
              "EBITDA, price_per_sales, price_per_book, sec_fillings) VALUES (", "'", "', '".join(row), "');", sep='')
