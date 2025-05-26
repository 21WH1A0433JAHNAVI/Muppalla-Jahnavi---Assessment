university_data = {
    "S101": {
        "name": "Alice Johnson",
        "major": "Computer Science",
        "courses": {
            "Python101": {"midterm": 88, "final": 92, "project": 94},
            "Math201": {"midterm": 78, "final": 85, "project": 80}
        }
    },
    "S102": {
        "name": "Bob Smith",
        "major": "Mathematics",
        "courses": {
            "Math201": {"midterm": 90, "final": 93, "project": 88},
            "Stats101": {"midterm": 84, "final": 80, "project": 85}
        }
    },
    "S103": {
        "name": "Clara Lopez",
        "major": "Physics",
        "courses": {
            "Physics101": {"midterm": 75, "final": 82, "project": 78},
            "Math201": {"midterm": 70, "final": 72, "project": 68}
        }
    }
}

#Print all student names and their majors
student_ids = university_data.keys()

for i in student_ids:
    print(f"Name: {university_data[i]['name']}, Major: {university_data[i]['major']}")

print()

#Average score per course per student 
for i in student_ids:
    courses_name = university_data[i]['courses'].keys()
    for j in courses_name:
        avg = sum(university_data[i]['courses'][j].values()) / len(university_data[i]['courses'])
            print(f"Name: {university_data[i]['name']}, Course: {j}, Average: {avg}")

print()

#Find students who scored >90 in final of Python101
for i in student_ids:
    courses_name = university_data[i]['courses'].keys()
    for j in courses_name:
        if j == 'Python101' and university_data[i]['courses'][j]['final'] > 90:
            print(f"Name: {university_data[i]['name']}")

print()

#Add new course AI101 for student S101
university_data["S101"]["courses"]["AI101"] = {"midterm": 95, "final": 82, "project": 68}
print(university_data["S101"]["courses"])

print()

#Print average for each course
res = {}
for i in student_ids:
    courses_name = university_data[i]['courses'].keys()
    for j in courses_name:
        print(j)
        if j not in res:
            res[j] = sum(university_data[i]['courses'][j].values())/len(university_data[i]['courses'][j].values())
        else:
            res[j] = (res[j] + sum(university_data[i]['courses'][j].values())/len(university_data[i]['courses'][j].values())) / 2

for i in res:
    print(f"Course: {i}, Average: {res[i]}")
