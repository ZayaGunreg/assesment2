import csv

file = open("employees.csv", 'r')
# task1
try:
    csv_reader = csv.reader(file)
    total_manager = 0
    total_manager_count = 0
    min_salary = 99999999
    min_salary_employee = ''
    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            print(" The column names are:", row[0], row[1], row[2], row[3])

        else:
            if row[3] == "Manager":
                total_manager += int(row[2])
                total_manager_count += 1

            if int(row[2]) < min_salary:
                min_salary = int(row[2])
                min_salary_employee = row[0] + " " + row[1]

        line_count += 1
    print("The average salary of manager is:", int(total_manager/total_manager_count), "dollars")
    print("The lowest salary is:", min_salary, "dollars")
    print(min_salary_employee, "has the lowest salary.")

finally:
    file.close()
