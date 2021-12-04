amount = input("Enter loan amount: ")
months = int(input("Enter maturity of loan: "))


try:
    loan_interest_percent = amount / months
except ZeroDivisionError as error:
    print(f"Loan maturity could not be 0\n{error}")
except TypeError as error:
    print(f"Type error occurred\n{error}")
finally:
    print("All works fine")
