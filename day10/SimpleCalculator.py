from art import logo

#---Calculation functions---#
def order(n1, n2):
    return n1 ** n2
def multiply(n1, n2):
    return n1 * n2
def division(n1, n2):
    return n1 / n2
def addition(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2

operation = {
        "**": order,
        "*": multiply,
        "/": division,
        "+": addition,
        "-": subtract
    }
can_continue = True
def calculation():
    print(logo)

    first_num = float(input("Enter a number: "))

    while can_continue:
        operator = input("Choose your operation('**', '*', '/', '+', '-'): ")
        second_num = float(input("Enter the next number: "))

        for key in operation:
            if key == operator:
                op = operation[operator](n1 = first_num, n2 = second_num)

        print(f"\n{first_num} {operator} {second_num} = {op}\n")
        choice = input(f"1) Press 'Y' to continue to calculate with the previous result {op}.\n"
                       "2) Press 'N' to perform new calculation.\n"
                       "3) Press 'E' to exit the program.\n=> ").lower()

        if choice == "y":
            first_num = op
        elif choice == "n":
            print("\n" * 100)
            calculation()
        elif choice == "E":
            print("---Good bye---")
            exit()
        else:
            print("---Invalid choice---")
            choice = input(f"1) Press 'Y' to continue to calculate with the previous result {op}.\n"
                           "2) Press 'N' to perform new calculation.\n"
                           "3) Press 'E' to exit the program.\n=> ").lower()

calculation()
