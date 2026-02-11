def get_integer(prompt="Enter a number: "):
    """ Get vaild input from the user  with custom prompt"""
    while True:
        try:
            num=int(input(prompt))
            if 0<= num <=100:
                return num
            else:
                print("Enter the valid integer from 0 to 100")
        except ValueError:
            print("Please enter valid integer")


def is_even(number):
    ''' return True if the number is even else false for odd number'''
    return number % 2 == 0

def main():
    ''' running the even odd program '''
    num=get_integer("Enter the number (0 to 100): ")
    result=is_even(num)
    if result:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

if __name__=="__main__":
    main()

    

    


