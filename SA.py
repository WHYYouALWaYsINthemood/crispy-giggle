month = ("January", "February","March","April","May","June","July","August","September","October","November","December")

profits = (144963, 358507, 57594, 257496, 255970, 354869, 794657, 465968, 364869, 15390, 2740683, 2649693)

max_profits = max(profits)
max_profits_index = profits.index(max_profits)
print(max_profits_index)
max_profits_month = month[max_profits_index]
print("The Maximum Profit Of " + str(max_profits) + " Was Recorded In The Month Of " + str(max_profits_month))

min_profits = min(profits)
min_profits_index = profits.index(min_profits)
print(min_profits_index)
min_profits_month = month[min_profits_index]
print("The Minimum Profit Of " + str(min_profits) + " Was Recorded In The Month Of " + str(min_profits_month))