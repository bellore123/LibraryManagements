def calculate_electricity_bill():
    try:
        units = float(input("Enter the number of units consumed: "))
        bill = 0

        if units <= 100:
            bill = units * 2
        elif units <= 200:
            bill = (100 * 2) + ((units - 100) * 3)
        else:
            bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)

        print(f"Total Electricity Bill: ₹{bill:.2f}")

    except ValueError:
        print("Please enter a valid numerical value for units.")

calculate_electricity_bill()