def get_score(prompt="Enter score: "):
    """Get valid score (0.0-100.0) from user."""
    while True:
        try:
            num=float(input(prompt))
            if 0.0<= num <=100.0:
                return num
            else:
                print("Enter the valid integer from 0 to 100")
        except ValueError:
            print("Enter the valid integer")

def calculate_weighted_grade(assignments, midterm, final_exam, project):
    """Calculate final grade using course weights."""
    return (assignments * 0.30 + midterm * 0.25 + final_exam * 0.30 + project * 0.15)
    

def get_letter_grade(numeric_grade):
    """Convert numeric grade to letter grade (A/B/C/D/F)."""
    if 90<= numeric_grade <= 100:
        return "A"
    elif 80 <= numeric_grade < 89:
        return "B"
    elif 70 <= numeric_grade < 79:
        return "C"
    elif 60 <= numeric_grade < 69:
        return "D"
    else:
        return "F"    

def main():
    """Run complete grade calculator program."""
    assignment = get_score("Enter Assignment score: ")
    midterm = get_score("Enter Midterm score: ")
    final = get_score("Enter Final score: ")
    project = get_score("Enter Project score: ")

    grade = calculate_weighted_grade(assignment, midterm, final, project)
    letter = get_letter_grade(grade)
    print(f"Final grade: {grade:.2f}, Letter: {letter}")

if __name__=="__main__":
    main()

