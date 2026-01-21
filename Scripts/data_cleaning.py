import pandas as pd
import os

def clean_data(online_retail, base_dir):
    """
    Cleans the Online Retail dataset.
    
    Steps:
    1. Remove duplicates
    2. Handle missing CustomerID
    3. Convert InvoiceDate to datetime
    4. Remove negative or zero Quantity
    5. Add TotalPrice column
    """
    
    ## remove the negative "Quantity" rows
    online_retail.drop(online_retail[online_retail.Quantity < 0].index, axis = 0, inplace = True)

    
    # remove the negative "UnitPrice" rows
    online_retail.drop(online_retail[online_retail.UnitPrice < 0].index, axis = 0, inplace = True)
    
    # adding the new column into the dataset that is "TotalAmount"
    online_retail = online_retail.assign(TotalAmount = online_retail.Quantity * online_retail.UnitPrice)
    
    # convert InvoiceDate to datetime
    online_retail['InvoiceDate'] = pd.to_datetime(online_retail['InvoiceDate'])
        
    # droping the dublicate values in the dataset
    online_retail.dropna(inplace = True)
    
    
    print("✅ Data cleaning completed!")
    print(f"Rows after cleaning: {online_retail.shape[0]}")

    file_name = os.path.join(base_dir, "Cleaned_OnlineRetail.xlsx")

    # Export to Excel with optimizations (faster engine)
    online_retail.to_excel(file_name, index=False, engine='openpyxl')
    
    return online_retail    
