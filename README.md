# 🛒 Online Retail Sales Analysis

### **Data Science Major Project | BCA Specialization in Data Analysis**
---

* **Version:** 1.0
* **Status:** ✅ Completed
* **Author:** **Prajwal Itnal** (Aspiring Data Analyst)
* **GitHub:** [https://github.com/PrajwalItnal](https://github.com/PrajwalItnal)

---
## 📝 Project Overview
---

This project performs an end-to-end data analysis on an Online Retail dataset using Python.  
It covers data loading, rigorous cleaning, exploratory data analysis (EDA), visualization, and business insights generation.  
The project follows a modular structure and is fully reproducible.

---

## ❓ Problem Statement
---

Retail businesses generate large volumes of transactional data. The challenge is to clean this raw data and extract meaningful insights related to customer behavior, product performance, and sales trends that can support business decision-making.

---

## 🎯 Project Objectives
---

- Load and explore raw retail transaction data
- Clean and preprocess the dataset (handling missing, negative, and invalid values)
- Perform exploratory data analysis (EDA)
- Analyze sales trends over time
- Identify top products, customers, and countries
- Generate visual and statistical insights

---

## 📊 Dataset Information
---

**Name:** Online Retail Dataset  
**Format:** Excel (.xlsx)  

Contains transactional records including invoice details, stock codes, quantities, prices, and customer locations.  

**Files:**
- `OnlineRetail.xlsx` – Raw input dataset
- `Cleaned_OnlineRetail.xlsx` – Preprocessed dataset for analysis

---

## 📂 Project Structure
---

```text
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
```
---
## 🛠️ Technologies & Libraries
---

**Language:** Python 3.9+  

**Libraries:**
- **pandas >= 2.0.0** – Data manipulation and analysis  
- **numpy >= 1.24.0** – Numerical computations  
- **matplotlib >= 3.5.0** – Data visualization  
- **scipy >= 1.10.0** – Statistical analysis  
- **openpyxl >= 3.1.0** – Excel file handling  
- **jupyter >= 1.0.0** – Notebook-based analysis  
- **fonttools >= 4.0.0** – Font support for plotting  
- **statsmodels >= 0.14.0** – Statistical modeling  
- **scikit-learn >= 1.3.0** – Machine learning tools  
- **seaborn >= 0.13.0** – Advanced data visualization  
- **os** – Operating system utilities for file handling and paths  

---

## 🧼 Data Cleaning Steps
---

- Remove records with negative quantity values
- Remove records with negative unit prices
- Handle missing values in CustomerID and Description
- Convert invoice date to proper datetime format
- Create new feature: TotalAmount (Quantity × UnitPrice)

---

## 🔍 EDA Analysis
---

- **Sales Distribution:** Revenue breakdown by market
- **Product-Level Analysis:** Best selling items and inventory trends
- **Customer-Level Analysis:** Purchasing frequency patterns
- **Country Comparison:** UK vs. International revenue contribution
- **Trend Analysis:** Weekly and monthly performance tracking

---

## 🚀 Execution Steps
---

**Prerequisites:**
- Python 3.9 or higher
- pip package manager

**Steps to Run:**

## 🚀 Full Execution Steps

### 1. Clone the repository
```bash
git clone https://github.com/PrajwalItnal/Online_Retail_Sales_Analysis.git
cd Online_Retail_Analysis_Main
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the main script
```bash
python main.py
```
### 4. Jupyter Notebook Instructions
```bash
jupyter notebook
# open FirstMainProjectRetail.ipynb and run all cells
```

---
## 💡 Key Insights

* **Market Leader:** The **United Kingdom** is the definitive primary market, contributing over **£7.3 Million** in gross revenue.
* **Top International Performers:**
    * **Netherlands:** Highly efficient market with high average transaction values.
    * **EIRE:** Strong, consistent volume and frequency.
    * **Germany & France:** The largest continental European markets by user count.
* **Growth Areas:**
    * **Saudi Arabia & Czech Republic:** Emerging markets showing initial traction in the global distribution.
* **Seasonal Dynamics:**
   * Sales peak exponentially in **November 2011**, reaching over ₹1.1M.
   * Weekly analysis reveals a massive surge in **Week 49,** with revenue exceeding $400,000.
  
---
## 🎓 Academic Information

- **Project Type:** Major Project
- **Course:** Bachelor of Computer Applications (BCA)
- **Specialization:** Data Analysis
- **Focus:** Data preprocessing, Analysis quality, and Insight generation

---
## 🔮 Future Scope

- Add predictive sales forecasting
- Perform customer segmentation using K-Means clustering
- Build interactive dashboards using Power BI or Tableau

---
## ✅ Full Execution Example
```bash
# Clone repository
git clone https://github.com/PrajwalItnal/Online_Retail_Sales_Analysis.git
cd Online_Retail_Analysis_Main

# Install dependencies
pip install -r requirements.txt

# Run the main script
python main.py

# Jupyter Notebook
jupyter notebook
# open FirstMainProjectRetail.ipynb and run all cells
```
---

## 🔚 Conclusion
This project successfully demonstrates the power of data cleaning and exploratory analysis in transforming raw retail data into actionable business intelligence. By identifying high-value markets and seasonal trends, the analysis provides a roadmap for optimizing inventory and targeting marketing efforts more effectively.

## 🤝 Contact & Support
If you have any questions or would like to collaborate on data analysis projects, feel free to reach out!

* **Author:** Prajwal Itnal
* **GitHub:** [@PrajwalItnal](https://github.com/PrajwalItnal)
* **LinkedIn:** [prajwal-itnal](https://www.linkedin.com/in/prajwal-itnal/)
* **Email:** [prajwalitnal20@gmail.com](mailto:prajwalitnal20@gmail.com)

---
*Developed as part of the BCA Specialization in Data Analysis.*

 ---
