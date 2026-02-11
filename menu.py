from sum_numbers import get_number, get_count, calculate_sum, display_result
from Course_Grade_calculator import get_score, calculate_weighted_grade, get_letter_grade

def show_menu():
    ''' displaying the menu'''

    print("\n" + "="*40)
    print("        Calculator Menu")
    print("="*40)
    print("1. Even/Odd checker")
    print("2. Grade Calculator")
    print("3. Sum Calculator")
    print("4. Exit")
    print("="*40)

def even_odd_checker():
    num=get_number("Enter the number: ")
    if num % 2 ==0:
        print(f"{num} is EVEN!")
    else:
        print(f"{num} is ODD!")


def run_grade_calculator():
    """Run complete grade calculator."""
    print("\n=== GRADE CALCULATOR ===")
    assignment = get_score("Enter Assignment score: ")
    midterm = get_score("Enter Midterm score: ")
    final = get_score("Enter Final score: ")
    project = get_score("Enter Project score: ")

    rade = calculate_weighted_grade(assignment, midterm, final, project)
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
            print("Invalid choice! Please select 1-4")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()