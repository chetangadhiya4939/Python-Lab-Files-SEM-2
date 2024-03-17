print("GADHIYA CHETAN BHAVESHBHAI\n23BCP182\nD-3.")
def merge_files(file1, file2, output_file):
  with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file,
                                                            'w') as of:
    of.write(f1.read() + "\n" + f2.read())


# Usage
merge_files('S1.txt', 'S2.txt', 'merged.txt')
