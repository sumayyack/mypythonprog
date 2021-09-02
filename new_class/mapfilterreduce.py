employees = [
    {"e_id": 1000, "e_name": "ram", "salary": 25000, "department": "testing", "exp": 1},
    {"e_id": 1001, "e_name": "ravi", "salary": 22000, "department": "ba", "exp": 1},
    {"e_id": 1002, "e_name": "raj", "salary": 20000, "department": "mrkt", "exp": 1},
    {"e_id": 1003, "e_name": "nikil", "salary": 26000, "department": "developer", "exp": 1},
    {"e_id": 1004, "e_name": "nivi", "salary": 28000, "department": "developer", "exp": 2},

]

# print employee names only

for employee in employees:
    print(employee["e_name"])

# print employee names in uppercase


for employee in employees:
    print(employee["e_name"].upper())


# print employee name who are working as developer

for employee in employees:
    if(employee["department"]=="developer"):
        print("developer",employee["e_name"])




#total salary


total=0
for employee in employees:
    total+=employee["salary"]

print(total)



#1 case Map
#2 case filter
#3 case reduce

#print highest salary_  reduce

# for loop ozhivakki ennitt lambda use aakitt print cheythu


e_names=list(map(lambda employee:employee["e_name"],employees))
print(e_names)

e_upper=list(map(lambda employee:employee["e_name"].upper(),employees))
print(e_upper)


developers=list(filter(lambda employee:employee["department"]=="developer",employees))

print(developers)


developers_name=list(map(lambda developer:developer["e_name"],
                                         list(filter(lambda employee:employee["department"]=="developer",employees)))
print(developers_name)