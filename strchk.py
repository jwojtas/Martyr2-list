
fill = input("Enter File name:")
f = open(fill, "r")
data = f.read()
stock_list = list(map(str, data.split()))

print (len(stock_list))