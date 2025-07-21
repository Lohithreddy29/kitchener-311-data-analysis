import pandas as pd 
df = pd.read_csv(r"C:\Users\danda\Downloads\Corporate_Contact_Centre_Requests_-8895652416371320004.csv")
print(df.head())
df.info()
df.describe(include='all')
for col in df.columns:
    print(f"'{col}' (length: {len(col)})")
df.columns = df.columns.str.strip() 
df.columns = df.columns.str.lower() 
df.columns = df.columns.str.replace(' ', '_', regex=False) 
df.columns = df.columns.str.replace('.', '_', regex=False) 
for col in df.columns:
    print(f"'{col}' (length: {len(col)})")
df = df.dropna(subset=['request_type', 'create_date'])
df['create_date'] = pd.to_datetime(df['create_date'], errors='coerce')

print(df.head())
df = df.drop_duplicates()
df = df[['create_date', 'request_type', 'department', 'channel', 'intersection', 'x', 'y']]
df.to_csv('cleaned_311_kitchener.csv', index=False)







