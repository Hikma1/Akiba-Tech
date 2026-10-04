name = input("Enter your name: ")
salary = float(input("Enter your basic salary: "))
transport_allowance = float(input("Enter your transport allowance: "))
food_allowance = float(input("Enter your food allowance: "))

gross_salary = salary + transport_allowance + food_allowance

print(f"Gross Salary of {name} is {gross_salary}")