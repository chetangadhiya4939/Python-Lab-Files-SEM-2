print("GADHIYA CHETAN BHAVESHBHAI\n23BCP182\nD-3.")
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'Blue']

color = [x for (i, x) in enumerate(color) if i not in (0, 2, 4, 5)]

print(color)
