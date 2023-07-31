
def profit(buy, shipping, packaging, selling):
    percent = (buy + shipping + packaging) * 0.20
    sum1 = (buy + shipping + packaging) + percent
    ebay_amazon_fee = selling * 0.18
    add = selling - ebay_amazon_fee
    profit = add - sum1

    return round(profit, 2)


Buy = float(input("Enter Buying Price: "))
shipping = float(input("Enter Shipping Price: "))
packaging = float(input("Enter packaging Price: "))
Selling = float(input("Enter selling Price: "))


gain = profit(Buy,shipping,packaging,Selling)

print(gain)