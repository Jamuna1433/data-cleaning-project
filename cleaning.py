import pandas as pd

# Load data
df = pd.read_csv("sales_data.csv")

print("Original Data")
print(df)

# Remove duplicates
df = df.drop_duplicates()

# Fill missing Sales with mean
df['Sales'] = df['Sales'].fillna(df['Sales'].mean())

# Fill missing Name
df['Name'] = df['Name'].fillna("Unknown")

# Clean text
df['Name'] = df['Name'].str.strip().str.title()

# Convert date
df['Date'] = pd.to_datetime(df['Date'])

print("\nCleaned Data")
print(df)

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("Cleaned file created!")