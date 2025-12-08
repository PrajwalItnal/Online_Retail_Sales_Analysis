import Scripts.data_loading as data_loader
import Scripts.data_cleaning as data_cleaner
from Scripts.eda import OnlineRetailEDA

def main():
    
    # Load the data
    data = data_loader.data_loading(file_path = r"Data\OnlineRetail.xlsx", sheet="OnlineRetail")
    
    # Display the first few rows of the dataset
    print(data.head())

    # Clean the data
    cleaned_data = data_cleaner.clean_data(data)

    # Display the first few rows of the cleaned dataset
    print(cleaned_data.head())

    # Perform EDA
    online_retail = OnlineRetailEDA(cleaned_data).run_full_eda()
    # Display the first few rows of the EDA results
    print(online_retail.head())

main()