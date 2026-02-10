total_sum=0
even_sum=0
odd_sum=0
count=0

while True:
    user_num=int(input("Enter a positive integer (0 to stop): "))

    if user_num ==0:
        break
    elif user_num < 0:
        print("Negative numbers are not allowed, try again.")
        continue
    total_sum += user_num
    count +=1

    if user_num % 2 == 0:
        even_sum += user_num
    else:
        odd_sum += user_num
print(f"Total Sum is: {total_sum}")
print(f"Total Even Sum is: {even_sum}")
print(f"Total Odd Sum is: {odd_sum}")
print(f"Total count is: {count}")



