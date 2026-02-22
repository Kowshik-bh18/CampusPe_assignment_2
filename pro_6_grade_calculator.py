# grade calculator program
# this calculates total marks percentage and grade

marks = []
for i in range(5):
    marks.append(float(input("enter marks: "))) # type casting

total = sum(marks)
percent = total / 5

if percent >= 90:
    grade = "a+"
elif percent >= 80:
    grade = "a"
elif percent >= 70:
    grade = "b"
elif percent >= 60:
    grade = "c"
elif percent >= 50:
    grade = "d"
else:
    grade = "f"

result = "pass" if all(m >= 40 for m in marks) else "fail"

print("total:", total)
print("percentage:", percent)
print("grade:", grade)
print("result:", result)
