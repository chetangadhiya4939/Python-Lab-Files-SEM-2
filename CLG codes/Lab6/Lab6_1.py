print("GADHIYA CHETAN BHAVESHBHAI\n23BCP182\nD-3.")
original_list = [11, 5, 17, 18, 23, 50]
unwanted_indexes = [0, 3, 4]
for idx in sorted(unwanted_indexes, reverse=True):
  del original_list[idx]
print("New list after removing elements by index:", original_list)
