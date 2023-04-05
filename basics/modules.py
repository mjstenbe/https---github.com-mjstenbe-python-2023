import apartment

print("How big is the apartments?")
size = input()

print("How much did it cost?")
cost = input()

flat = apartment.Apartment(size, cost)
result = flat.calculate()

print('m2 cost of your apt is: {}€' .format(result))
