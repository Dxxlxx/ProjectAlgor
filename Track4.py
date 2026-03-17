import pandas as pd

# อ่านไฟล์จากเครื่อง
df = pd.read_csv(r"C:\Users\ZeroG\Desktop\MiniProject\CprE_Subject.csv",
                 dtype={"CourseCode": str})

# ดึงค่า credit
df["CreditValue"] = df["Credit"].str.extract(r'(\d+)').astype(int)

# เก็บข้อมูล
courses = {}

for _, row in df.iterrows():
    code = str(row["CourseCode"])

    if code not in courses:
        courses[code] = {
            "name": row["Name"],
            "credit": int(row["CreditValue"])
        }


def get_max_load():

    max_credit = -1
    max_code = None

    for code, data in courses.items():
        if data["credit"] > max_credit:
            max_credit = data["credit"]
            max_code = code

    name = courses[max_code]["name"]

    print(f"Highest Credit Course: {max_code} ({name}) - {max_credit} Credits.")


def list_sorted():

    print("Course Catalog:")

    codes = list(courses.keys())
    n = len(codes)

    # Bubble Sort
    for i in range(n):
        for j in range(0, n-i-1):

            if codes[j] > codes[j+1]:
                codes[j], codes[j+1] = codes[j+1], codes[j]

    for code in codes:
        print(f"{code} - {courses[code]['name']}")


def list_by_credit():

    print("Courses Sorted by Credits (High -> Low):")

    sorted_courses = sorted(
        courses.items(),
        key=lambda x: x[1]["credit"],
        reverse=True
    )

    for code, data in sorted_courses:
        print(f"{code} ({data['name']}) - {data['credit']} Credits")


get_max_load()
print()
list_sorted()
print()
list_by_credit()