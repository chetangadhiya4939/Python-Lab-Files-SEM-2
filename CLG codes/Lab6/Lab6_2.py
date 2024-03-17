print("GADHIYA CHETAN BHAVESHBHAI\n23BCP182\nD-3.")
test_list = [4, 6, 6, 4, 2, 2, 4, 4, 8, 5, 8]
test_list.sort()
res = {}
temp = []
prev = None

while test_list:
  curr = test_list.pop(0)
  if curr == prev or prev is None:
    temp.append(curr)
  else:
    res[prev] = temp
    temp = [curr]
  prev = curr

res[prev] = temp
print("Similar grouped dictionary : " + str(res))
