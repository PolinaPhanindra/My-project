def read_students():
    with open("students.txt","r") as f:
        text = f.read()
    
    lines = text.splitlines()
    header = lines[0]
    data_lines = lines[1:]
    students = []
    
    for line in data_lines:
        parts = line.split(",")
        name = parts[0]
        math = float(parts[1])
        science = float(parts[2])
        english = float(parts[3])
        student = {
            "name": name,
            "math": math,
            "science": science,
            "english": english
        }
        students.append(student)
    
    return students  # Returns LIST OF DICTS!


def calculate_student_average(student):
    return(student["math"] + student["science"] + student["english"]) / 3

def calculate_class_average(students):
    total = 0
    for student in students:
        total += calculate_student_average(student)
    return total / len(students)

def write_results(students):
    with open("results.txt", "w") as f:
        # Header ONCE
        f.write("name,math,science,english,average\n")
        
        # Each student ONCE
        for student in students:
            avg = calculate_student_average(student)
            f.write(f"{student['name']},{int(student['math'])},"
                   f"{int(student['science'])},{int(student['english'])},"
                   f"{avg:.2f}\n")
        
        # Summary
        class_avg = calculate_class_average(students)
        top_student = max(students, key=calculate_student_average)
        top_avg = calculate_student_average(top_student)
        f.write(f"\nClass average: {class_avg:.2f}\n")
        f.write(f"Top student: {top_student['name']} ({top_avg:.2f})\n")


def main():
    students = read_students()
    print("Students loaded:", students)
    
    class_avg = calculate_class_average(students)
    print(f"Class average: {class_avg:.2f}")
    
    print("\nIndividual averages:")
    for student in students:
        avg = calculate_student_average(student)
        print(f"{student['name']}: {avg:.2f}")
    
    write_results(students)  # ✅ Only call THIS
    print("\n✅ Results saved to results.txt")


if __name__=="__main__":
    main()
