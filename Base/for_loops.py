prices = [10, 20, 30]

total = 0

# begning of forloop
for price in prices:
    print("price:",price)
    print("tmp total:",total)
    total = total + price
# end of for loop

print(f"Total: {total}")