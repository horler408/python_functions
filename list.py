numbers = [1, 2, 3, 4, 5]

numbers_power_2 = [n**2 for n in numbers]  # [1, 4, 9, 16, 25]


# Looping
numbers_power_2 = []
for n in numbers:
    numbers_power_2.append(n**2)


# Map
numbers_power_2 = list(map(lambda n: n**2, numbers))
