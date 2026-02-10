user_num=float(input("Enter the Number: "))
if user_num.is_integer():
    num=int(user_num)
    if num % 2 ==0:
        print("Entered Number is Even")
    else:
        print("Entered Number is Odd")
else:
    print("Entered Number is not Integer, It should be only positive Integer Number")