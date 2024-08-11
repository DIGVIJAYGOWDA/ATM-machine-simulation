# Initialising variables
pin="4444"
balance=200.0
transaction_history = []

#Function loop to validate whether the PIN entered by the user matches the pre-defined PIN
def validate_pin():
    
    for _ in range(3):
        entered_pin = input("Enter your 4-digit PIN: ")
        if entered_pin == pin:
            return True
        print("Invalid PIN. Please try again.")
    return False

#Function to display formatted menu of options for ATM system
def display_menu():
    """Display the ATM menu options."""
    print("\n\t--- ATM Menu ---")
    print("\n1. Account Balance Inquiry")
    print("2. Cash Withdrawal")
    print("3. Cash Deposit")
    print("4. Change PIN")
    print("5. Transaction History")
    print("6. Exit")

def main():
    """Main function to run the ATM simulation."""
    global balance, pin, transaction_history  # Declare variables as global

    if validate_pin():
        while True:
            display_menu()
            choice = input("Please select an desired option {1-6}: ")

            if choice == '1':  # Balance Inquiry
                print(f"Balance: RS:{balance:.2f}")

            elif choice == '2':  # Cash Withdrawal
                try:
                    amount = float(input("Enter amount to withdraw: RS:"))
                    if amount <= balance:
                        balance -= amount
                        transaction_history.append(f"Withdrew: RS:{amount:.2f}")
                        print(f"Please take your cash: RS:{amount:.2f}")
                    else:
                        print("Insufficient balance!")
                except ValueError:
                    print("Please enter a valid amount.")

            elif choice == '3':  # Cash Deposit
                try:
                    amount = float(input("Enter amount to deposit: RS:"))
                    if amount > 0:  # Ensure deposit amount is positive
                        balance += amount
                        transaction_history.append(f"Deposited: RS:{amount:.2f}")
                        print(f"Successfully deposited: RS:{amount:.2f}")
                    else:
                        print("Deposit amount must be greater than zero.")
                except ValueError:
                    print("Please enter a valid amount.")

            elif choice == '4':  # Change PIN
                new_pin = input("Enter your new PIN (4 digits): ")
                if new_pin.isdigit() and len(new_pin) == 4:  # Simple validation for new PIN
                    pin = new_pin
                    print("PIN changed successfully!")
                else:
                    print("Invalid PIN. It must be a 4-digit number.")

            elif choice == '5':  # Transaction History
                print("\n--- Transaction History ---")
                if transaction_history:
                    for transaction in transaction_history:
                        print(transaction)
                else:
                    print("No transactions found.")

            elif choice == '6':  # Exit
                print("Thank you for using the ATM. Goodbye!")
                break

            else:  # Invalid option
                print("Invalid option. Please try again.")
    else:
        print("Too many failed attempts. Exiting.")

# Run the ATM simulation
if __name__ == "__main__":
    main()
