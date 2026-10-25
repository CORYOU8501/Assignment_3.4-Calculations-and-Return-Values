from datetime import datetime


# Converts Fahrenheit into Celsius
def convertData(temperature):
    celsius = (temperature - 32) * 5 / 9
    return celsius


# Collects the dates and temperatures
def getInput():
    entries = int(input("How many entries are you inputing?\n"))

    for i in range(entries):
        date = input("Enter a date:\n")
        temperature = float(input("Enter the highest temp for the inputed date:\n"))

        # Call convertData with a Fahrenheit temperature and return its Celsius value.
        converted = convertData(temperature)

        print(f"The following was saved at {datetime.now()} :")
        print(f"{date},{temperature:g},{converted}")


# Spreadsheet automation menu
print("coryou8501's Spreadsheet Automation Menu")
print("Choose a number from the following options")      
print("1 Input Date")
print("2 View Current Date")
print("3 Generate Report")

choice = input()

# Check for valid menu selections
if choice in ["1", "2", "3"]:
    print(f"You selected {choice} at {datetime.now()}")

    if choice == "1":
        getInput()
    else:
        print("Error: The chosen functionality is not implemented yet")
else:
    print("Error: Invalid choice selected.")
        
