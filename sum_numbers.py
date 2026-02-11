def get_number(prompt="Enter number: "):
    ''' get input from user one number at a time '''
    while True:
        try:
            num=float(input(prompt))
            return num
        except ValueError:
            print("Please enter valid integer")

def get_count():
    ''' get the initial count and how many user enters number'''
    while True:
        try:
            count=int(input("Enter the number between 1 to 20:  "))
            if 1 <= count <=20:
                return count
            else:
                print("Enter the number between 1 to 20  ")
        except ValueError:
            print("Please enter valid Integer")


def calculate_sum(numbers):
    '''calculate the sum of the entered numbers'''
    return sum(numbers)

def display_result(Total):
    ''' Display the total on the output screen'''
    print(f"Sum {Total:.2f}")

def main():
    '''main function to run the sum calculator'''
    print("___Sum Calculator___")
    count = get_count()
    numbers=[]

    for i in range(count):
        numbers.append(get_number(f"Enter number {i+1}:"))

    total=calculate_sum(numbers)
    display_result(total)


if __name__=="__main__":
    main()

