import pandas as pd

def clean_data(online_retail):
    """
    Cleans the Online Retail dataset.
    
    Steps:
    1. Remove duplicates
    2. Handle missing CustomerID
    3. Convert InvoiceDate to datetime
    4. Remove negative or zero Quantity
    5. Add TotalPrice column
    """
    
    # 1. Remove duplicates
    online_retail.drop(online_retail[online_retail.Quantity < 0].index, axis = 0, inplace = True)

    
    # remove the negative "UnitPrice" rows
    online_retail.drop(online_retail[online_retail.UnitPrice < 0].index, axis = 0, inplace = True)
    
    # adding the new column into the dataset that is "TotalAmount"
    online_retail = online_retail.assign(TotalAmount = online_retail.Quantity * online_retail.UnitPrice)
    
    # 4. Convert InvoiceDate to datetime
    online_retail['InvoiceDate'] = pd.to_datetime(online_retail['InvoiceDate'])
    
    # remove the negative "UnitPrice" rows
    online_retail.drop(online_retail[online_retail.UnitPrice < 0].index, axis = 0, inplace = True)
    
    # droping the dublicate values in the dataset
    online_retail.dropna(inplace = True)
    
    print("✅ Data cleaning completed!")
    print(f"Rows after cleaning: {online_retail.shape[0]}")
    
    return online_retail    
