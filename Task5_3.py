# Lesson 5: Python Functions
# 3. The Grade Analyzer

def calculate_average(grades):
    total = sum(grades)
    return total / len(grades)

def find_highest_grade(grades):
    return max(grades)

def find_lowest_grade(grades):
    return min(grades)

def assign_letter_grade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'

# Example usage
grades_list = [85, 92, 78, 65, 90]
average_grade = calculate_average(grades_list)
highest_grade = find_highest_grade(grades_list)
lowest_grade = find_lowest_grade(grades_list)

print(f"Average grade: {average_grade:.2f}")
print(f"Highest grade: {highest_grade}")
print(f"Lowest grade: {lowest_grade}")

for grade in grades_list:
    print(f"Numerical grade: {grade} -> Letter grade: {assign_letter_grade(grade)}")
