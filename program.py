import asyncio

class SurvivalDurationCalculator:
    def __init__(self, age):
        # Constructor to initialize the age of the person
        self.age = age

    def calculate(self, unit):
        # Check for each unit and calculate the duration
        if unit == 'm' or unit == 'months':
            return self.age * 12, "Months"
        elif unit == 'w' or unit == 'weeks':
            return self.age * 52, "Weeks"
        elif unit == 'd' or unit == 'days':
            return self.age * 365, "Days"
        elif unit == 'h' or unit == 'hours':
            return self.age * 365 * 24, "Hours"
        elif unit == 'min' or unit == 'minutes':
            return self.age * 365 * 24 * 60, "Minutes"
        elif unit == 's' or unit == 'seconds':
            return self.age * 365 * 24 * 60 * 60, "Seconds"
        else:
            # Return None if the unit is invalid
            return None, None

# Function to resolve PyodideFuture if necessary
async def get_input(prompt):
    value = input(prompt)
    if isinstance(value, asyncio.Future):  # Check if it's a PyodideFuture or similar
        value = await value
    return value

# Main program logic
async def main():
    print("Survival Duration Calculator")
    
    # Get the user's age
    try:
        age_input = await get_input("What's your age? ")  # Wait for the resolved value
        age = float(age_input)  # Convert input to float for decimal support
        if age < 0:
            print("Age cannot be negative. Please enter a valid age.")
            return
    except ValueError:
        print("Invalid input. Please enter a numerical value for age.")
        return
   
    # Prompt user to select a unit
    print("Choose a time unit: Months (m), Weeks (w), Days (d), Hours (h), Minutes (min), Seconds (s).")
    unit = (await get_input("Enter your choice: ")).lower()

    # Create an instance of the class with the given age
    calculator = SurvivalDurationCalculator(age)
    # Call the calculate method and get the result
    result, unit_name = calculator.calculate(unit)
    
    # Check if the calculation was successful
    if result is not None:
        print(f"You have lived for {result:,.2f} {unit_name}.")
    else:
        print("Invalid time unit selected.")

# Run the program safely in an existing event loop
def run_main():
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None

    if loop and loop.is_running():
        # For environments with an already running loop, like Jupyter or Pyodide
        return asyncio.ensure_future(main())
    else:
        # For standard Python scripts
        asyncio.run(main())

# Ensures the program runs only when executed directly
if __name__ == "__main__":
    run_main()
