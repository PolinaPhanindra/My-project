bill_amount=float(input("Enter the Bill Amount: "))
tip_percentage=float(input("Enter the Tip Percentage %: "))
tip_amount=(bill_amount*tip_percentage)/100
total_bill_Amount= bill_amount+tip_amount
print(f"Your Bill Amount: ${bill_amount:.2f}")
print(f" Your Tip Amount: ${tip_amount:.2f}")
print(f"Your Total_Bill_Amount is: ${total_bill_Amount:.2f}")