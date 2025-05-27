class dept:
    def __init__(self, deptid, name, loc, hod):
        self.deptid = deptid
        self.name = name
        self.loc = loc
        self.hod = hod

    def display_dept_info(self):
        print("Dept Information")
        print("----------------")
        print(f"Dept ID: {self.deptid}")
        print(f"Depatment Name: {self.name}")
        print(f"Department Location: {self.loc}")
        print(f"HOD: {self.hod}")

    def return_values(self):
        return [deptid, name, loc, hod]


#input
num_of_depts = int(input("Enter num of deptarments to enter: "))
department = {}
for i in range(1, num_of_depts + 1):
    deptid = input("Enter deptid: ")
    name = input("Enter department name: ")
    loc = input("Enter location: ")
    hod = input("Enter HOD: ")
    department[i] = dept(deptid, name, loc, hod).return_values()


print()
#display info
for i in range(num_of_depts):
    print("Dept Information")
    print("-----------------------")
    print(f"Dept ID: {department[i + 1][0]}")
    print(f"Dept Name: {department[i + 1][1]}")
    print(f"Dept Location: {department[i + 1][2]}")
    print(f"HOD: {department[i + 1][3]}")
    print()


#number of depts
print(f"The total number of departments are {len(department)}")


print()
#search by deptid
flag = 0
search_deptid = input("Enter DeptID to search: ")
for i in range(num_of_depts):
    if search_deptid == department[i+1][0]:
        print(f"Dept ID: {department[i + 1][0]}")
        print(f"Dept Name: {department[i + 1][1]}")
        print(f"Dept Location: {department[i + 1][2]}")
        print(f"HOD: {department[i + 1][3]}")
        flag = 1
if flag == 0:
    print("Deparment ID not found")


print()
#search by deptname
flag = 0
search_deptname = input("Enter Dept Name to search: ")
for i in range(num_of_depts):
    if search_deptname == department[i+1][1]:
        print(f"Dept ID: {department[i + 1][0]}")
        print(f"Dept Name: {department[i + 1][1]}")
        print(f"Dept Location: {department[i + 1][2]}")
        print(f"HOD: {department[i + 1][3]}")
        flag = 1
if flag == 0:
    print("Deparment name not found")   
