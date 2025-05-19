import random
import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv
import streamlit as st

# not required anymore

# df1 = pd.read_csv('calories_upd1.csv')

# df2=df1.drop(df1.columns[2:5], axis = 1)
# df2.columns=['Category', 'Ingredient']
# df2['Quantity'] = 0  
######################################################

#print (df2.head()) 

conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()
#df2.to_sql('inventory', conn, if_exists='replace', index=False)

cursor.execute("SELECT rowid FROM inventory")  # Using rowid as a generic identifier
row_ids = cursor.fetchall()

update_data = []
for row_id in row_ids:
    random_quantity = random.randint(100, 1000)
    update_data.append((random_quantity, row_id[0]))

query = "UPDATE inventory SET Quantity = ? WHERE rowid = ?"
cursor.executemany(query, update_data)

cursor.execute("SELECT * FROM inventory")
updated_records = cursor.fetchall()
print(updated_records)

conn.commit()
conn.close()

st.write("""
#IBCP Capstone
#Test deployment
Checking *italics* and line writes
""")
