import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r"D:\pythonProject4\Superstore.csv", encoding='ISO-8859-1')

# Convert date column
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Set style
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# 1. Sales by Category/Sub-Category
category_sales = df.groupby(['Category', 'Sub-Category'])['Sales'].sum().sort_values(ascending=False).reset_index()
category_sales['Label'] = category_sales['Category'] + " / " + category_sales['Sub-Category']

plt.figure()
sns.barplot(x=category_sales['Sales'], y=category_sales['Label'])
plt.title('Sales by Category and Sub-Category')
plt.xlabel('Sales')
plt.ylabel('')
plt.tight_layout()
plt.show()

# 2. Profit by Region
region_profit = df.groupby('Region')['Profit'].sum().sort_values()

plt.figure()
sns.barplot(x=region_profit.values, y=region_profit.index, palette="coolwarm")
plt.title('Profit by Region')
plt.xlabel('Profit')
plt.ylabel('')
plt.tight_layout()
plt.show()

# 3. Top 10 Products by Sales
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

plt.figure()
sns.barplot(x=top_products.values, y=top_products.index, palette="viridis")
plt.title('Top 10 Products by Sales')
plt.xlabel('Sales')
plt.ylabel('Product Name')
plt.tight_layout()
plt.show()

# 4. Monthly Sales Trend
monthly_sales = df.resample('M', on='Order Date')['Sales'].sum()

plt.figure()
monthly_sales.plot(color='teal', marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()

# 5. Discount vs Profit
discount_profit = df[['Discount', 'Profit']]

plt.figure()
sns.scatterplot(data=discount_profit, x='Discount', y='Profit', alpha=0.6, color='purple')
plt.title('Discount vs Profit')
plt.xlabel('Discount')
plt.ylabel('Profit')
plt.tight_layout()
plt.show()
