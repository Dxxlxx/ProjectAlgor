import pandas as pd

# อ่านไฟล์
df = pd.read_csv(
    r"C:\Users\ZeroG\Desktop\MiniProject\CprE_Subject.csv",
    dtype={"CourseCode": str}
)

# ดึงค่า Credit
df["CreditValue"] = df["Credit"].str.extract(r'(\d+)').astype(int)

# สร้าง Dictionary
courses = {}

for _, row in df.iterrows():
    code = str(row["CourseCode"])

    if code not in courses:
        courses[code] = {
            "name": row["Name"],
            "credit": int(row["CreditValue"])
        }

# หา course ที่มี credit สูงสุด (O(n))
def get_max_load():

    if not courses:
        print("No course data available.")
        return

    max_credit = -1
    max_code = None

    for code, data in courses.items():
        if data["credit"] > max_credit:
            max_credit = data["credit"]
            max_code = code

    max_course = courses[max_code]

    print(f"Highest Credit Course: {max_code} ({max_course['name']}) - {max_course['credit']} Credits.")


# เรียง CourseCode ด้วย Bubble Sort (O(n^2))
def list_sorted():

    print("Course Catalog:")

    codes = list(courses.keys())
    n = len(codes)

    for i in range(n):
        for j in range(0, n-i-1):

            if codes[j] > codes[j+1]:
                temp = codes[j]
                codes[j] = codes[j+1]
                codes[j+1] = temp

    for code in codes:
        course = courses[code]
        print(f"{code} - {course['name']}")


# เรียงตาม credit จากมากไปน้อย
def list_by_credit():

    print("Courses Sorted by Credits (High -> Low):")

    sorted_courses = sorted(
        courses.items(),
        key=lambda x: x[1]["credit"],
        reverse=True
    )

    for code, data in sorted_courses:
        print(f"{code} ({data['name']}) - {data['credit']} Credits")


# อัปเดตจำนวนหน่วยกิต (Dynamic)
def update_credit(course_code, new_credit):

    if course_code not in courses:
        print(f"Course {course_code} not found.")
        return

    courses[course_code]["credit"] = new_credit
    print(f"Course {course_code} updated to {new_credit} credits.")

    max_credit = -1
    max_code = None

    for code, data in courses.items():
        if data["credit"] > max_credit:
            max_credit = data["credit"]
            max_code = code

    print(f"New Max Course is now: {max_code}.")


get_max_load()
print()

update_credit("010123124", 5)
print()

list_sorted()
print()

list_by_credit()
