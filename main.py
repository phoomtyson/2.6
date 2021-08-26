# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    tax_rate = 0.2
    standard_deduction = 10000
    deduction_per_dependent = 3000
    # The inputs are
    gross_income = float(input("Gross income : "))
    number_of_dependents = float(input("number of dependents : "))
    # Computations
    net_income = gross_income - standard_deduction - (deduction_per_dependent * number_of_dependents)
    income_tax = net_income * tax_rate
    print("Your income before tax is", net_income)
    print("Your income tax is", round(income_tax, 2))
    print("Your income after tax is", net_income - income_tax)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
