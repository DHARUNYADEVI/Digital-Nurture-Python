def assign_grade(score):
    if score>=90:
        print("Grade A")
    elif score>=75:
        print("Grade B")
    elif score>=50:
        print("Grade C")
    else:
        print("Fail")
score=88
assign_grade(score)