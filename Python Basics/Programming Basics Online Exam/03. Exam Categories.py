difficulty = int(input())
confusion = int(input())
pages = int(input())
exam_type = " "

if difficulty >= 80 and confusion >= 80 and pages >= 8:
    exam_type = "Legacy"

elif difficulty >= 80 and confusion <= 10:
    exam_type = "Master"

elif difficulty <= 30 and pages <= 1:
    exam_type = "Easy"

elif difficulty <= 10:
    exam_type = "Elementary"

elif confusion >= 50 and pages >= 2:
    exam_type = "Hard"

else:
    exam_type = "Regular"

print(exam_type)