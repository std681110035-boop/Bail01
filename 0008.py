name = input("กรอกชื่อ: ")
lname = input("กรอกนามสกุล: ")

affective = float(input("กรอกคะแนนจิตพิสัย: "))
attendance = float(input("กรอกคะแนนมาเรียน: "))
subject = float(input("กรอกคะแนนรายวิชา: "))
project = float(input("กรอกคะแนนงานบูรณาการ: "))
finalexam = float(input("กรอกคะแนนสอบปลายภาค: "))

total = affective + attendance + subject + project + finalexam

status = "ผ่าน"

if total < 0 or total > 100:
    print("คะแนนไม่ถูกต้อง")
    grade = "คะแนนไม่ถูกต้อง"
elif total >= 80:
    grade = "A"
elif total >= 75:
    grade = "B+"
elif total >= 70:
    grade = "B"
elif total >= 65:
    grade = "C+"
elif total >= 60:
    grade = "C"
elif total >= 55:
    grade = "D+"
elif total >= 50:
    grade = "D"
else:
    grade = "F"
    status = "ตก"

print("-" * 30)
print("ชื่อ:", name)
print("นามสกุล:", lname)
print(f"คะแนนรวม: {total} คะแนน")
print(f"เกรดที่ได้: {grade}")
print(f"สถานะ: {status}")
print("-" * 30)
