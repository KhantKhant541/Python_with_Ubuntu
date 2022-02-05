
employee = {'name': input("Enter employee\'s name : "), 'age': int(input("Enter age : ")),
            'experience': int(input("Job experience(in year) : ")), 'address': input("Enter address : ")}

print("Printing the detail of employee : ")
print(f"Name           : {employee['name']}")
print(f"Age            : {employee['age']}")
print(f"Job experience : {employee['experience']}")
print(f"Address        : {employee['address']}")

# for key, value in employee.items():
#     print(f"{key} = {value}")
