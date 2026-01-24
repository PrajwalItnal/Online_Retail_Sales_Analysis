project:
  heading: "**🛒 Online Retail Sales Analysis**"
  subtitle: "**Data Science Major Project | BCA Specialization in Data Analysis**"
  separator: "---"
  version: "1.0"
  status: "✅ Completed"
  author: "**Prajwal Itnal (Aspiring Data Analyst)**"
  github: "[https://github.com/PrajwalItnal](https://github.com/PrajwalItnal)"

overview:
  heading: "**📝 Project Overview**"
  separator: "---"
  description: >
    This project performs an end-to-end data analysis on an Online Retail dataset using Python.
    It covers data loading, rigorous cleaning, exploratory data analysis (EDA), visualization,
    and business insights generation. The project follows a modular structure and is fully reproducible.

problem_statement:
  heading: "**❓ Problem Statement**"
  separator: "---"
  description: >
    Retail businesses generate large volumes of transactional data. The challenge is to clean this raw data
    and extract meaningful insights related to customer behavior, product performance, and sales trends
    that can support business decision-making.

objectives:
  heading: "**🎯 Project Objectives**"
  separator: "---"
  list:
    - "Load and explore raw retail transaction data"
    - "Clean and preprocess the dataset (handling missing, negative, and invalid values)"
    - "Perform exploratory data analysis (EDA)"
    - "Analyze sales trends over time"
    - "Identify top products, customers, and countries"
    - "Generate visual and statistical insights"

dataset:
  heading: "**📊 Dataset Information**"
  separator: "---"
  name: "Online Retail Dataset"
  format: "Excel (.xlsx)"
  description: >
    Contains transactional records including invoice details, stock codes, quantities, prices, and customer locations.
  files:
    - name: "OnlineRetail.xlsx"
      type: "Raw input dataset"
    - name: "Cleaned_OnlineRetail.xlsx"
      type: "Preprocessed dataset for analysis"

project_structure:
  heading: "**📂 Project Structure**"
  separator: "---"
  structure: |
    Online_Retail_Analysis_Main/
    ├── Data/                       # Dataset directory
    │   ├── OnlineRetail.xlsx       # Raw dataset
    │   └── Cleaned_OnlineRetail.xlsx
    ├── Scripts/                    # Python modules
    │   ├── data_loading.py         # Pandas loading logic
    │   ├── data_cleaning.py        # Preprocessing logic
    │   ├── eda.py                  # Analysis logic
    │   └── insights.py             # Business logic
    ├── Output/                     # Results
    │   └── Charts/                 # Saved Visualizations
    ├── Jupyter_Notebook/           # Experimental analysis
    │   └── FirstMainProjectRetail.ipynb
    ├── main.py                     # Main execution entry point
    ├── requirements.txt            # List of dependencies
    └── README.md                   # Documentation

technologies_libraries:
  heading: "**🛠️ Technologies & Libraries**"
  separator: "---"
  language: "Python 3.9+"
  libraries:
    - name: "pandas"
      description: "Data manipulation and analysis"
    - name: "numpy"
      description: "Numerical computations"
    - name: "matplotlib"
      description: "Data visualization"
    - name: "scipy"
      description: "Statistical analysis"
    - name: "openpyxl"
      description: "Excel file handling"
    - name: "jupyter"
      description: "Notebook-based analysis"

data_cleaning:
  heading: "**🧼 Data Cleaning Steps**"
  separator: "---"
  steps:
    - "Remove records with negative quantity values"
    - "Remove records with negative unit prices"
    - "Handle missing values in CustomerID and Description"
    - "Convert invoice date to proper datetime format"
    - "Create new feature: TotalAmount (Quantity × UnitPrice)"

eda_analysis:
  heading: "**🔍 EDA Analysis**"
  separator: "---"
  sales_distribution: "Revenue breakdown by market"
  product_level_analysis: "Best selling items and inventory trends"
  customer_level_analysis: "Purchasing frequency patterns"
  country_comparison: "UK vs. International revenue contribution"
  trend_analysis: "Weekly and monthly performance tracking"

execution:
  heading: "**🚀 Execution Steps**"
  separator: "---"
  prerequisites:
    - "Python 3.9 or higher"
    - "pip package manager"
  steps_to_run:
    - step: "Clone the repository"
      commands:
        - "git clone https://github.com/PrajwalItnal/Online_Retail_Sales_Analysis.git"
        - "cd Online_Retail_Analysis_Main"
    - step: "Install dependencies"
      commands:
        - "pip install -r requirements.txt"
    - step: "Run the main script"
      commands:
        - "python main.py"
  jupyter_notebook:
    instructions:
      - "Launch Jupyter by running `jupyter notebook` in your terminal"
      - "Open `FirstMainProjectRetail.ipynb`"
      - "Execute cells sequentially using Shift + Enter"
      - "To run everything at once, select Cell > Run All"

key_insights:
  heading: "**💡 Key Insights**"
  separator: "---"
  market_leader: "The UK is the primary market, contributing over £7.3 Million"
  top_international_performers:
    - "Netherlands"
    - "EIRE"
    - "Germany"
    - "France"
  growth_areas:
    - "Saudi Arabia"
    - "Czech Republic"

academic_information:
  heading: "**🎓 Academic Information**"
  separator: "---"
  project_type: "Major Project"
  course: "Bachelor of Computer Applications (BCA)"
  specialization: "Data Analysis"
  focus: "Data preprocessing, Analysis quality, and Insight generation"

future_scope:
  heading: "**🔮 Future Scope**"
  separator: "---"
  items:
    - "Add predictive sales forecasting"
    - "Perform customer segmentation using K-Means clustering"
    - "Build interactive dashboards using Power BI or Tableau"
