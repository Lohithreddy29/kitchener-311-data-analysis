import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("cleaned_311_kitchener.csv")

# Convert 'create_date' to datetime
df['create_date'] = pd.to_datetime(df['create_date'], errors='coerce')

# Drop rows with missing create_date
df = df.dropna(subset=['create_date'])

# Create time features
df['year'] = df['create_date'].dt.year
df['month'] = df['create_date'].dt.month
df['year_month'] = df['create_date'].dt.to_period('M')


sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))


# 1. Top 10 Request Types

top_requests = df['request_type'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_requests.values, y=top_requests.index, palette="viridis")
plt.title("Top 10 Request Types in Kitchener")
plt.xlabel("Number of Requests")
plt.ylabel("Request Type")
plt.tight_layout()
plt.show()


# 2. Requests Per Year

requests_per_year = df['year'].value_counts().sort_index()
plt.figure(figsize=(8, 5))
sns.lineplot(x=requests_per_year.index, y=requests_per_year.values, marker='o')
plt.title("Number of Requests Per Year")
plt.xlabel("Year")
plt.ylabel("Request Count")
plt.tight_layout()
plt.show()


# 3. Requests Per Month (All Years Combined)

requests_per_month = df['month'].value_counts().sort_index()
plt.figure(figsize=(8, 5))
sns.barplot(x=requests_per_month.index, y=requests_per_month.values, palette="magma")
plt.title("Requests by Month (All Years)")
plt.xlabel("Month")
plt.ylabel("Number of Requests")
plt.tight_layout()
plt.show()


# 4. Requests by Channel

channels = df['channel'].value_counts()
plt.figure(figsize=(10, 5))
sns.barplot(x=channels.index, y=channels.values, palette="cubehelix")
plt.title("Request Volume by Channel")
plt.xlabel("Channel")
plt.ylabel("Number of Requests")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 5. Requests by Department

departments = df['department'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=departments.values, y=departments.index, palette="coolwarm")
plt.title("Top 10 Departments by Request Volume")
plt.xlabel("Number of Requests")
plt.ylabel("Department")
plt.tight_layout()
plt.show()
