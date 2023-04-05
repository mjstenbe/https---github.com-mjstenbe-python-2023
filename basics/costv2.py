def calculate(size, const):
    """
    This function calculates sqm cost of apt
    """

    return int(cost)/int(size)


print("How big is the apartments?")
size = input()

print("How much did it cost?")
cost = input()

result = calculate(size, cost)

print('m2 cost of your apt is: {}€' .format(result))
