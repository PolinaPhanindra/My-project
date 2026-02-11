def get_number(prompt="Enter number: "):
    """Get valid number from user."""
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Please enter a valid number")

def get_score(prompt="Enter score: "):
    """Get valid score (0.0-100.0) from user."""
    while True:
        try:
            num = float(input(prompt))
            if 0.0 <= num <= 100.0:
                return num
            else:
                print("Please enter a valid score between 0 and 100")
        except ValueError:
            print("Please enter a valid number")

def get_count():
    """Get valid count (1-20) from user."""
    while True:
        try:
            count = int(input("How many numbers (1-20)? "))
            if 1 <= count <= 20:
                return count
            else:
                print("Please enter a number between 1 and 20")
        except ValueError:
            print("Please enter a valid integer")

def calculate_weighted_grade(assignments, midterm, final_exam, project):
    """Calculate final grade using course weights."""
    return (assignments * 0.30 + midterm * 0.25 + final_exam * 0.30 + project * 0.15)

def get_letter_grade(numeric_grade):
    """Convert numeric grade to letter grade."""
    if 90 <= numeric_grade <= 100:
        return "A"
    elif 80 <= numeric_grade <= 89:
        return "B"
    elif 70 <= numeric_grade <= 79:
        return "C"
    elif 60 <= numeric_grade <= 69:
        return "D"
    else:
        return "F"

def calculate_sum(numbers):
    """Calculate sum of numbers list."""
    return sum(numbers)

def display_result(total):
    """Display formatted sum result."""
    print(f"Sum: {total:.2f}")

def show_menu():
    """Display the main menu."""
    print("\n" + "="*40)
    print("         CALCULATOR MENU")
    print("="*40)
    print("1. Even/Odd Checker")
    print("2. Grade Calculator")
    print("3. Sum Calculator")
    print("4. Exit")
    print("-"*40)

def even_odd_checker():
    """Check if number is even or odd."""
    num = get_number("Enter a number: ")
    if num % 2 == 0:
        print(f"{num} is EVEN")
    else:
        print(f"{num} is ODD")

def run_grade_calculator():
    """Run complete grade calculator."""
    print("\n=== GRADE CALCULATOR ===")
    assignment = get_score("Enter Assignment score: ")
    midterm = get_score("Enter Midterm score: ")
    final = get_score("Enter Final score: ")
    project = get_score("Enter Project score: ")
    
    grade = calculate_weighted_grade(assignment, midterm, final, project)
    letter = get_letter_grade(grade)
    print(f"Final grade: {grade:.2f}, Letter: {letter}")

def run_sum_calculator():
    """Run complete sum calculator."""
    print("\n=== SUM CALCULATOR ===")
    count = get_count()
    numbers = []
    
    for i in range(count):
        numbers.append(get_number(f"Enter number {i+1}: "))
    
    total = calculate_sum(numbers)
    display_result(total)

def main():
    """Main menu loop."""
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            even_odd_checker()
        elif choice == "2":
            run_grade_calculator()
        elif choice == "3":
            run_sum_calculator()
        elif choice == "4":
            print("Thanks for using Calculator Menu! 👋")
            break
        else:
            print("❌ Invalid choice! Please select 1-4")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
