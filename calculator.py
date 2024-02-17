class Calculator:
    def addition(input1, input2):
        return input1 + input2

    def subtraction(input1, input2):
        return input1 - input2

    def multiplication(input1, input2):
        return input1 * input2

    def division(input1, input2):
        try:
            return input1 / input2
        except ZeroDivisionError:
            print("You are dividing by zero!!!")

    def percentage(input1, input2):
        return input1 * input2 / 100

calculator = Calculator()

print("Select Operation to perform calculation")
print("1.Addition\n"
      "2.Subtraction\n"
      "3.Multiplication\n"
      "4.Division\n"
      "5.Percentage"
      )
while True:
    try:
        operation = int(input("Enter the operation to perform from 1/2/3/4/5:"))

        if operation >= 6:
            print("Enter only specified numbers.")
            continue

        input1 = float(input("Enter the first number:"))
        input2 = float(input("Enter the second number:"))

        if operation == 1:
                print(input1, "+", input2, "=", Calculator.addition(input1,input2))
        elif operation == 2:
                print(input1, "-", input2, "=", Calculator.subtraction(input1, input2))
        elif operation == 3:
                print(input1, "*", input2, "=", Calculator.multiplication(input1, input2))
        elif operation == 4:
                print(input1, "/", input2, "=", Calculator.division(input1, input2))
        elif operation == 5:
                print(input1,"%","of", input2, "=", Calculator.percentage(input1, input2))


        def continue_calc():
            try:
                next = input("Need to perform next operation (yes/no):").lower()
                if next not in ('yes', 'no'):
                    raise ValueError("Entered wrong value. Please enter yes or no")
                if next == "no":
                    exit()
            except ValueError as v:
                print(v)
                continue_calc()

        continue_calc()
    except ValueError:
        print("Invalid Input!!! Enter correct Value")

