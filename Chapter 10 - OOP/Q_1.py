# Create a class programmer for storing information of few programmers working at microsoft.


class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def employeeDetails(self):
        # print(f"Name: {self.name}, Position: {self.position}")
        return f"Name: {self.name}, Position: {self.position}"
        # return f"{self.name} {self.position}"
    
employee1 = Employee("Avinash", "SDE 1")
print(employee1.name)


# employee1.employeeDetails()
print(employee1.employeeDetails())




