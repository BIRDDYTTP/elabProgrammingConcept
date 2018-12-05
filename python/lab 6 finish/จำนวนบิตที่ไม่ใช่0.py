x = int(input("Enter an 8-bit number: "))

numbits = ('{:08b}'.format(x)).count('1')

print("The number %d has %d non-zero bits" % (x, numbits))