 
import pandas as pd 
import time 
 
df = pd.read_csv("/home/yuva/Downloads/archive/credit_card_transactions-ibm_v2.csv") 
 
print("Dataset loaded. Total rows:", len(df)) 
print("🔹 Columns available:", df.columns.tolist()) 
 
df['Amount'] = df['Amount'].replace('[\$,]', '', regex=True).astype(float) 
 
fraud_count = 0 
total_amount = 0 
 
for index, row in df.iterrows(): 
    time.sleep(1)  # simulate delay 
     
    total_amount += row['Amount'] 
    if row['Is Fraud?'] == "Yes": 
        fraud_count += 1 
     
    print( 
        f"Row {index+1}: User={row['User']}, Card={row['Card']}, " 
        f"Amount={row['Amount']:.2f}, Merchant={row['Merchant Name']}, " 
        f"Fraud={row['Is Fraud?']}" 
    ) 
     
     if row['Amount'] > 1000: 
        print("High-value transaction detected!") 
    if row['Is Fraud?'] == "Yes": 
        print("Fraudulent transaction detected!") 
     
     print(f" Processed: {index+1} transactions | Total Amount=${total_amount:.2f} | Fraud 
Cases={fraud_count}") 
    print("-" * 60) 
 
     if index == 20: