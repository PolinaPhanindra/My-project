def get_count():
    """Get valid student count (1-5)."""
    while True:
        try:
            count = int(input("How many students (1-5)? "))
            if 1 <= count <= 5:
                return count
            print("Please enter 1-5")
        except ValueError:
            print("Enter a valid number")

def get_score(prompt):
    """Get valid score (0-100)."""
    while True:
        try:
            score = float(input(prompt))
            if 0 <= score <= 100:
                return score
            print("Score must be 0-100")
        except ValueError:
            print("Enter a valid number")

def calculate_average(math, science, english):
    """Calculate average of 3 scores."""
    return (math + science + english) / 3

def find_highest_average(students):
    """Find student with highest average."""
    top_student = students[0]
    top_avg = calculate_average(
        students[0]["math"], 
        students[0]["science"], 
        students[0]["english"]
    )
    
    for student in students:
        avg = calculate_average(student["math"], student["science"], student["english"])
        if avg > top_avg:
            top_avg = avg
            top_student = student
    
    return top_student["name"], top_avg

def main():
    print("=== Student Gradebook ===")
    
    # Step 1: Get number of students
    count = get_count()
    students = []
    
    # Step 2: Get each student data
    for i in range(count):
        print(f"\n--- Student {i+1} ---")
        name = input("Enter name: ").strip()
        
        math = get_score("Enter Math (0-100): ")
        science = get_score("Enter Science (0-100): ")
        english = get_score("Enter English (0-100): ")
        
        # Step 3: Create dictionary for this student
        student = {
            "name": name,
            "math": math,
            "science": science, 
            "english": english
        }
        students.append(student)
    
    # Step 4: Display all students
    print("\n" + "="*50)
    print("GRADEBOOK")
    print("="*50)
    for i, student in enumerate(students, 1):
        avg = calculate_average(student["math"], student["science"], student["english"])
        print(f"{i}. {student['name']:10} | Math:{student['math']:2.0f} "
              f"Science:{student['science']:2.0f} English:{student['english']:2.0f} | "
              f"Avg: {avg:.1f}")
    
    # Step 5: Find highest average
    top_name, top_avg = find_highest_average(students)
    print(f"\n🏆 Highest average: {top_name} ({top_avg:.1f})")

if __name__ == "__main__":
    main()
