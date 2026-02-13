def get_count():
    while True:
        try:
            count=int(input("How many students (1-5)"))
            if 1<= count <=5:
                return count
                print("Please enter (1-5)")
        except ValueError:
            print("Please enter valid integer")

def get_score(prompt):
    while True:
        try:
            score=float(input(prompt))
            if 0<= score<=100:
                return score
                print("score must be 0 to 100")
        except ValueError:
            print("Please enter valid number")

def calculate_average(math, science, english):
    return (math + science + english)/3

def main():
    print("=== Student Gradebook ===")
    count=get_count()
    students=[]
    # collecting the student records
    for i in range(count):
        print(f"\n--- Student {i+1} ---")
        name = input("Enter name: ").upper().strip()
        math = get_score("Enter Math (0-100): ")
        science = get_score("Enter Science (0-100): ")
        english = get_score("Enter English (0-100): ")
        student = {
            "name": name,
            "math": math,
            "science": science,
            "english": english
        }
        students.append(student)
        # Display each student's average
    print("\n=== Averages ===")
    for student in students:
        avg = calculate_average(student["math"], student["science"], student["english"])
        print(f"{student['name']}: {avg:.2f}")

if __name__ == "__main__":
    main()
