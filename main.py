# Section A: Python Code for Lease Accounting

# 1. Variables and Values
lease_payment = 1000  # Integer value representing monthly lease payment
lease_duration = 12  # Integer value representing the duration of the lease in months

# Using the variables in a calculation
total_payment = lease_payment * lease_duration
print(f"Total payment for the lease duration is: {total_payment}")

# 2. Loops (For Loop and While Loop)
# Using a for loop to calculate total payments over the lease duration
total_payment = 0
for month in range(lease_duration):
    total_payment += lease_payment
    print(f"Payment after month {month + 1}: {total_payment}")

# Using a while loop to calculate total payments
total_payment = 0
month = 0
while month < lease_duration:
    total_payment += lease_payment
    month += 1
    print(f"Payment after month {month}: {total_payment}")


# 3. Functions (Including If Functions)
def calculate_total_payment(lease_payment, lease_duration):
    if lease_duration <= 0:
        return 0  # Handle edge case where lease duration is 0 or negative
    total_payment = lease_payment * lease_duration
    return total_payment


# Using the function
total = calculate_total_payment(lease_payment, lease_duration)
print(f"Total lease payment calculated using function: {total}")

# 4. Difference Between Strings, Integers, Floats, and Booleans
lease_description = "Office Space Lease"  # String
monthly_payment = 1000  # Integer
interest_rate = 5.5  # Float
lease_active = True  # Boolean

# Printing the types of each variable
print(f"Type of lease_description: {type(lease_description)}")
print(f"Type of monthly_payment: {type(monthly_payment)}")
print(f"Type of interest_rate: {type(interest_rate)}")
print(f"Type of lease_active: {type(lease_active)}")

# 5. Creating a Simple Tkinter Form
import tkinter as tk


# Function to calculate and display total lease payment in the form
def calculate_payment():
    try:
        lease_payment = float(entry_payment.get())  # Get and convert input to float
        lease_duration = int(entry_duration.get())  # Get and convert input to integer
        total_payment = lease_payment * lease_duration
        label_result.config(text=f"Total Payment: {total_payment}")
    except ValueError:
        label_result.config(text="Invalid input. Please enter numbers only.")


# Creating the main window
root = tk.Tk()
root.title("Lease Payment Calculator")

# Creating and placing widgets
label_payment = tk.Label(root, text="Monthly Payment:")
label_payment.grid(row=0, column=0)
entry_payment = tk.Entry(root)
entry_payment.grid(row=0, column=1)

label_duration = tk.Label(root, text="Lease Duration (Months):")
label_duration.grid(row=1, column=0)
entry_duration = tk.Entry(root)
entry_duration.grid(row=1, column=1)

button_calculate = tk.Button(root, text="Calculate", command=calculate_payment)
button_calculate.grid(row=2, column=0, columnspan=2)

label_result = tk.Label(root, text="Total Payment:")
label_result.grid(row=3, column=0, columnspan=2)

# Running the application
root.mainloop()
