# Given a list of study hours x, a weight w = 2.0, and a bias b = 1.0, 
# generate a list of predictions y_pred using the formula y=w.x+ b

x = [float(h) for h in input("Enter the number of hours studied (comma-separated): ").split(",")]
w = 2.0
b = 1.0

y_pred = [w * hour + b for hour in x]

print("Predicted exam scores for the hours studied:", x, "are:", y_pred)


# ML models struggle when one feature is huge (e.g., salaries from $30,000 to $100,000) 
# and another is small (e.g., age from 20 to 60). We scale numbers between 0.0 and 1.0 using
# scaled = x - min / max - min

salary = [30000, 50000, 70000, 100000]
min_salary = min(salary)
max_salary = max(salary)

scaled = [(s - min_salary) / (max_salary - min_salary) for s in salary]

print("Scaled salaries between 0.0 and 1.0:", scaled)