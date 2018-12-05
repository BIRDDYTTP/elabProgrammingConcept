
# input
inc = float(input())

ex =  float(input())


# output
print("1234567890" * 3)
print("%-13s%+8.2f bahts" % ("Total Income", inc))
print("%-13s%+8.2f bahts" % ("Expense", ex))
print("%-13s%08.2f bahts" % ("Profit", inc + ex))