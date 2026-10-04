student_name = input("Enter your name: ")
python_score = float(input("Enter your Python score: "))
english_score = float(input("Enter your English score: "))
math_score = float(input("Enter your Math score: "))

avg_score = (python_score + english_score + math_score) / 3

print(f"Average score of {student_name} is {avg_score}")