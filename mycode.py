import pandas as pd
import os

data = {'Name':['Anil', 'Ramesh', 'Naresh'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']
        }
df = pd.DataFrame(data)
# new row gets added to table
df.loc[len(df.index)] = {"Name": "V3", "Age": 20, "City":"Laknow"}
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir ,'sample_data.csv')

df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")
