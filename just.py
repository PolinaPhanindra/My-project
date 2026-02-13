def main():
    # Step 1: Empty notebook
    students = []
    
    # Step 2: Add 2 students (hardcoded for now)
    students.append({"name": "Alice", "math": 85, "science": 92, "english": 78})
    students.append({"name": "Bob", "math": 88, "science": 75, "english": 90})
    
    # Step 3: MAGIC LOOP - read every page
    print("=== Student Averages ===")
    for student in students:
        avg = (student["math"] + student["science"] + student["english"]) / 3
        print(f"{student['name']}: {avg:.1f}")

if __name__ == "__main__":
    main()
