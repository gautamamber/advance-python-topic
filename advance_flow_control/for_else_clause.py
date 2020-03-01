"""
Check in a list if a number is divisible by a particular number or not
"""
items = [2, 45, 36, 37]
divisor = 12

for item in items:
    if item % divisor == 0:
        found = item
        break
else:
    items.append(divisor)
    found = divisor

print("{items} contains {found} which is a multiple of {divisor}".format(**locals()))

