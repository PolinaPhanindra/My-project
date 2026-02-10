user_assignment=float(input("Enter the Assignment Score(0-100):"))
user_midterm= float(input("Enter the Midterm Score(0-100):"))
user_final_exam=float(input("Enter the Final Exam Scores(0-100):"))
user_project=float(input("Enter the Project Score(0-100):"))
if (user_assignment < 0 or user_assignment >100 or user_midterm < 0 or user_midterm > 100 or user_final_exam < 0 or user_final_exam > 100 or user_project < 0 or user_project > 100):
    print("Error: All Terms Scores must be in between 0 to 100")
else:
    total_marks=(user_assignment * 0.30 + user_midterm * 0.25 + user_final_exam * 0.30 + user_project * 0.15)
    
    print(f"Final mark: {total_marks:.2f}")
    
    if 90<= total_marks <= 100:
        print("Student Grade is A")
    elif 80 <= total_marks < 89:
        print("Student Grade is B")
    elif 70 <= total_marks < 79:
        print("Student Grade is C")
    elif 60 <= total_marks < 69:
        print("Student Grade is D")
    else:
        print("Student Grade is F")
