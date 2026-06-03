class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def average(self):
        return sum(self.marks) / len(self.marks)
    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 50:
            return "C"
        return "Fail"
student = Student(
    "Dharunya",
    [95, 97, 93]
)
print("Average:", student.average())
print("Grade:", student.grade())