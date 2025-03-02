import pandas as pd

# Load the Excel file (update the path if needed)
file_path = r"C:\Users\Ahmet\Documents\Kitap1.xlsx"
df = pd.read_excel(file_path, sheet_name='Sayfa1')

# Print column names and count for debugging
print("Original columns:", df.columns)
print("Number of columns:", len(df.columns))

# Ensure we only take the first three relevant columns
df = df.iloc[:, :3]  # Select first three columns
df.columns = ["Date", "Amount", "Notes"]  # Rename columns

# Convert Date column to datetime and Amount to numeric
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')

# Remove rows with NaN Amount (no transaction)
df_cleaned = df.dropna(subset=['Amount']).copy()

# Sort by date
df_cleaned.sort_values(by='Date', inplace=True)

# Set initial balance and monthly interest rate
balance = 0
monthly_interest_rate = 0.045
end_date = df_cleaned['Date'].min() + pd.DateOffset(months=12)  # First week of the 7th month

# Initialize tracking for the last date when interest was applied
last_interest_month = df_cleaned['Date'].dt.month.min() - 1

# List to track the balance history
balance_data = []

# Loop through each transaction
for date, amount in zip(df_cleaned['Date'], df_cleaned['Amount']):
    if date > end_date:
        break

    # Apply interest if a new month has started since the last application
    if date.month != last_interest_month:
        if balance > 0:
            pre_interest_balance = balance
            balance *= (1 + monthly_interest_rate)
            print(f"Interest applied on {date.strftime('%Y-%m-%d')} - Balance before interest: {pre_interest_balance:.2f} TL, New balance: {balance:.2f} TL")
        last_interest_month = date.month
    
    # Update balance with each transaction
    balance += amount
    transaction_type = "Income" if amount > 0 else "Expense"
    print(f"{transaction_type} on {date.strftime('%Y-%m-%d')} - Amount: {amount:.2f} TL, Updated balance: {balance:.2f} TL")
    
    # Record the balance history
    balance_data.append((date, balance))

# Display the final balance at the end of the period
print(f"Balance at the first week of the 7th month: {balance:.2f} TL")
