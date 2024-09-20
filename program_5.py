# There are two kinds of hot dogs sold:
# Hot Dog ($3.50), Chili Dog ($4.50).
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).
# Also tax is 7%.
# Write a program the inputs the type of hot dog wanted and optional toppings.
# The program then displays the hot dog cost, tax and total cost.

def HotDiggityDog(DogPrice):

    DogPrice = 0.0

    if Hotdogtype == 1:
        DogPrice = 3.50
    elif Hotdogtype == 2:
        DogPrice = 4.50

    return DogPrice


def HotDiggitySide(Sidetype):

    SidePrice = 0.0


    if Sidetype == 1:
        SidePrice = 0.50
    elif Sidetype == 2:
        SidePrice = 0.75
    elif Sidetype == 3:
        SidePrice = 1.00

    return SidePrice

if __name__ == '__main__':
    Hotdogtype = 0.0

    Hotdogtype = float(input("Enter the type of hot dog (1 for Hot Dog, 2 for Chili Dog): "))
    Sidetype = float(input("Enter the type of side (1 for Cheese, 2 for Peppers, 3 for Grilled Onions, 0 for None): "))

    DogPrice = HotDiggityDog(Hotdogtype)
    Sidetype = HotDiggitySide(Sidetype)
    tax = (DogPrice + Sidetype) * 0.7
    Total = tax + DogPrice + Sidetype

    print(f'Hot Dog Price: ${DogPrice:.2f}')
    print(f'Tax: ${tax:.2f}')
    print(f'Total: ${Total:.2f}')


