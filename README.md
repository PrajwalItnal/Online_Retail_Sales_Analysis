project:
  title: "Online Retail Sales Analysis"
  version: "1.0"
  status: "Completed"
  description: >
    This project performs an end-to-end data analysis on an Online Retail dataset
    using Python. It covers data loading, data cleaning, exploratory data analysis
    (EDA), visualization, and business insights generation. The project follows a
    modular structure and is fully reproducible.

problem_statement:
  description: >
    Retail businesses generate large volumes of transactional data. The challenge
    is to clean this raw data and extract meaningful insights related to customer
    behavior, product performance, and sales trends that can support business
    decision-making.

objectives:
  - Load and explore raw retail transaction data
  - Clean and preprocess the dataset
  - Handle missing, negative, and invalid values
  - Perform exploratory data analysis (EDA)
  - Analyze sales trends over time
  - Identify top products, customers, and countries
  - Generate visual and statistical insights

dataset:
  name: "Online Retail Dataset"
  format: "Excel (.xlsx)"
  description: >
    The dataset contains transactional records of an online retail store,
    including invoice details, product information, quantities, prices,
    customer IDs, and country data.
  files:
    - OnlineRetail.xlsx: "Raw dataset (input)"
    - Cleaned_OnlineRetail.xlsx: "Generated cleaned dataset (ignored in GitHub)"

project_structure:
  Data:
    description: "Dataset directory"
    files:
      - OnlineRetail.xlsx
  Scripts:
    description: "Python modules for analysis"
    files:
      - data_loading.py: "Loads Excel data using pandas"
      - data_cleaning.py: "Cleans and preprocesses the dataset"
      - eda.py: "Performs exploratory data analysis"
      - insights.py: "Generates business insights"
  Output:
    description: "Generated results"
    Charts:
      - "Sales trend charts"
      - "Top products charts"
      - "Country-wise analysis charts"
  Jupyter_Notebook:
    description: "Exploratory and experimental analysis"
    files:
      - FirstMainProjectRetail.ipynb
  Root_Files:
    - main.py: "Main execution file"
    - requirements.txt: "List of dependencies"
    - .gitignore: "Ignored files and folders"
    - README.md: "Markdown documentation"
    - README.yml: "YAML documentation"

technologies:
  programming_language: Python
  libraries:
    pandas: "Data manipulation and analysis"
    numpy: "Numerical computations"
    matplotlib: "Data visualization"
    scipy: "Statistical analysis"
    openpyxl: "Excel file handling"
    jupyter: "Notebook-based analysis"

data_cleaning_steps:
  - Remove records with negative quantity values
  - Remove records with negative unit prices
  - Handle missing values
  - Convert invoice date to datetime format
  - Create new feature: TotalAmount (Quantity × UnitPrice)

eda_analysis:
  - Sales distribution analysis
  - Product-level analysis
  - Customer-level analysis
  - Country-wise sales comparison
  - Monthly and weekly sales trend analysis

visualizations:
  - Line charts for time-based trends
  - Bar charts for top products and countries
  - Aggregated sales plots
  storage_location: "Output/Charts"

key_insights:
  - Identification of top-selling products
  - Countries contributing highest revenue
  - Customer purchasing frequency patterns
  - Seasonal and weekly sales trends

execution_steps:
  prerequisites:
    - Python 3.9 or higher
    - pip package manager
  steps:
    - step_1: "Clone the GitHub repository"
      command: "git clone https://github.com/PrajwalItnal/Online_Retail_Sales_Analysis.git"
    - step_2: "Navigate to the project directory"
      command: "cd Online_Retail_Analysis_Main"
    - step_3: "Install required Python libraries"
      command: "pip install -r requirements.txt"
    - step_4: "Run the main Python script"
      command: "python main.py"
    - step_5: "View generated charts in Output/Charts directory"

git_and_version_control:
  repository: "GitHub"
  practices:
    - Use of .gitignore for clean repository
    - Exclusion of generated files and caches
    - Modular and readable commit history

limitations:
  - Dataset is static and historical
  - No real-time data processing
  - No machine learning predictions included

future_scope:
  - Add predictive sales forecasting
  - Perform customer segmentation using clustering
  - Build interactive dashboards using Power BI or Tableau
  - Automate report generation

academic_information:
  project_type: "Major Project"
  course: "Bachelor of Computer Applications (BCA)"
  specialization: "Data Analysis"
  evaluation_focus:
    - Data preprocessing
    - Analysis quality
    - Code structure
    - Insight generation

author:
  name: "Prajwal Itnal"
  role: "Aspiring Data Analyst"
  github: "https://github.com/PrajwalItnal"
