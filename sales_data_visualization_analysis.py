import kagglehub  # Assuming this is a correctly installed module
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Download the latest version of the dataset from Kaggle
path = kagglehub.dataset_download("aungpyaeap/supermarket-sales")
print("Path to dataset files:", path)

# Load the Dataset with correct encoding
url = path + "/supermarket_sales - Sheet1.csv"
df = pd.read_csv(url, encoding='ISO-8859-1')
print(df.head())  # Print the first few rows to inspect the data

# Print out the columns of the DataFrame to check for the correct column names
print(df.columns)

# Ensure 'Date' is in datetime format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Check for any NaT values in 'Date' column and handle them
print(df[df['Date'].isna()])

# 1. Bar Chart: Total sales by product line
total_sales_by_product_line = df.groupby('Product line')['Total'].sum().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='Product line', y='Total', data=total_sales_by_product_line, palette='viridis', legend=False)
plt.title('Total Sales by Product Line')
plt.xlabel('Product Line')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()

# 2. Line Graph: Sales Trend Over Time
sales_trend = df.groupby('Date')['Total'].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(x='Date', y='Total', data=sales_trend, marker='o')
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()

# 3. Scatter Plot: Sales (Total) by Product Line and Gender
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Product line', y='Total', data=df, hue='Gender', palette='deep')
plt.title('Sales by Product Line and Gender')
plt.xlabel('Product Line')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()