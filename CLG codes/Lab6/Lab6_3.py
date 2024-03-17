print("GADHIYA CHETAN BHAVESHBHAI\n23BCP182\nD-3.")
def common_data(list1, list2):
    result = False
    for x in list1:
        # Iterate through each element 'y' in 'list2'
        for y in list2:
            # Check if the current elements 'x' and 'y' are equal
            if x == y:
                # If there's a common element, set 'result' to True and return it
                result = True
                return result


print(common_data([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))

print(common_data([1, 2, 3, 4, 5], [6, 7, 8, 9])) 
