n = int(input())

count_solution = 0

for i in range(n):
    problem_solution = str(input())
    if problem_solution[2] == "1" and (problem_solution[0] == "1" or problem_solution[4] == "1"):
        count_solution += 1
    elif problem_solution[0] == "1" and (problem_solution[2] == "1" or problem_solution[4] == "1"):
        count_solution += 1

print(count_solution)