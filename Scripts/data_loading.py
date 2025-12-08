def data_loading(file_path, sheet):
    import pandas as pd
    try:
        print("✅ Data loading started...")
        df = pd.read_excel(file_path, sheet_name=sheet, engine="openpyxl")
        print("✅ Data loaded successfully!")
        print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
        return df
    except FileNotFoundError:
        print("❌ Error: File not found. Check the file path.")
    except Exception as e:
        print("❌ An error occurred while loading data:", e)
