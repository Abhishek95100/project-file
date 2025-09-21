price = int(input("Enter the product price:"))
if price > 1000:
    discount = price* 0.10 #10% discount
else:
    discount = price*0.5 #5% discount

# final price after discount

final_price = discount-price

print("orangle price:",price)
print("Discount:",discount)
print("final price after discount :",final_price)