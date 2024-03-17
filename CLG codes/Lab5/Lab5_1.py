print("GADHIYA CHETAN BHAVESHBHAI\n23BCP182\nD-3.")
class StudentManagementSystem:

  def __init__(self):
    self.students = []

  def add_student(self, name, score):
    self.students.append((name, score))

  def remove_student(self, name):
    self.students = [(n, s) for n, s in self.students if n != name]

  def update_student_score(self, name, new_score):
    for i, (n, s) in enumerate(self.students):
      if n == name:
        self.students[i] = (n, new_score)
        break

  def display_students(self):
    print("Students:")
    for name, score in self.students:
      print(f"Name: {name}, Score: {score}")

  def calculate_average_score(self):
    total_score = sum(score for _, score in self.students)
    return total_score / len(self.students) if self.students else 0


# Instantiate the StudentManagementSystem
sms = StudentManagementSystem()

# Add students
sms.add_student("Alice", 85)
sms.add_student("Bob", 90)
sms.add_student("Charlie", 75)

# Display students
sms.display_students()

# Update a student's score
sms.update_student_score("Bob", 95)

# Display students after updating
sms.display_students()

# Remove a student
sms.remove_student("Charlie")

# Display students after removal
sms.display_students()

# Calculate average score
average_score = sms.calculate_average_score()
print(f"Average Score: {average_score}")
