import warnings
warnings.filterwarnings("ignore", message="findfont: Font family 'Noto Color Emoji' not found.")

import pandas as pd
import matplotlib.pyplot as plt
import Scripts.conf as fontcon

# Configure the font in matplotlib
fontcon.fontConfig()


class OnlineRetailEDA:
    """
    Performs Exploratory Data Analysis on the cleaned Online Retail dataset.
    """

    def __init__(self, online_retail):
        self.online_retail = online_retail

    # ========= Public grouped EDA functions =========

    def run_full_eda(self):
        """Run all EDA blocks."""
        self.eda_overview()
        self.eda_country()
        self.eda_product()
        self.eda_customer()
        self.eda_time()
        self.eda_recency()
        self.eda_max_timeframes()
        return self.online_retail

    def eda_overview(self):
        self._dataset_overview()
        self._basic_counts()

    def eda_country(self):
        self._country_sales()
        self._top_countries_highest_sales()
        self._top_countries_by_users()
        self._average_sales_per_country()

    def eda_product(self):
        self._top_best_selling_products_by_quantity()
        self._top_products_by_total_amount()
        self._top_products_by_unit_price()
        self._uk_most_sold_items()
        self._uk_top_products_by_amount()

    def eda_customer(self):
        self._top_customers_by_items_and_cost()
        self._top_customers_buying_frequently()

    def eda_time(self):
        self._average_quantity_per_invoice()
        self._monthly_sales_trends()
        self._weekly_sales_trends()
        self._weekly_and_monthly_means()

    def eda_recency(self):
        self._recently_active_customers()

    def eda_max_timeframes(self):
        self._max_sales_timeframes()

    # ========= Private helpers (print with emojis and separators) =========

    def _dataset_overview(self):
        print("\n--------------- 📊 Dataset Overview 📊 ---------------")
        print("ℹ️ Data Information:")
        print(self.online_retail.info())
        print("📈 Statistical Summary:")
        print(self.online_retail.describe())
        print("-----------------------------------------------------\n")

    def _basic_counts(self):
        num_customers = self.online_retail["CustomerID"].nunique()
        print(f"\n--------------- ✅ Unique Customers ✅ ---------------")
        print(f"{num_customers} 👥")
        print("-----------------------------------------------------")

        num_countries = self.online_retail["Country"].nunique()
        print(f"\n--------------- 🌍 Unique Countries 🌍 ---------------")
        print(f"{num_countries}")
        print("-----------------------------------------------------")

        num_items = self.online_retail["Description"].nunique()
        print(f"\n--------------- 🛍️ Unique Items 🛍️ ---------------")
        print(f"{num_items}")
        print("-----------------------------------------------------\n")

    def _country_sales(self):
        country_sales = self.online_retail.groupby("Country")["TotalAmount"].sum()
        print("\n--------------- 💰 Country-wise Total Sales 💰 ---------------")
        print(country_sales)
        print("---------------------------------------------------------------\n")

    def _average_quantity_per_invoice(self):
        avg_qty = self.online_retail.groupby("InvoiceNo")["Quantity"].sum().mean()
        print("\n--------------- 📦 Average Quantity per Invoice 📦 ---------------")
        print(f"{avg_qty:.2f} items")
        print("-----------------------------------------------------------------\n")

    def _top_countries_highest_sales(self):
        top_countries = (
            self.online_retail.groupby("Country")["TotalAmount"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )
        print("\n--------------- 🏆 Top 10 Countries by Total Sales 🏆 ---------------")
        print(top_countries)
        print("-----------------------------------------------------------------------\n")

        plt.figure(figsize=(10, 6))
        plt.bar(top_countries.index, top_countries.values)
        plt.xlabel("Country")
        plt.ylabel("Total Sales")
        plt.title("🏆 Top 10 Countries by Total Sales")
        plt.show()

    def _top_best_selling_products_by_quantity(self):
        top_products = (
            self.online_retail.groupby("Description")["Quantity"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )
        print("\n--------------- 🔥 Top 10 Best-Selling Products by Quantity 🔥 ---------------")
        print(top_products)
        print("-------------------------------------------------------------------------------\n")

        plt.figure(figsize=(10, 8))
        plt.bar(x=top_products.index, height=top_products.values, color="blue")
        plt.title("🔥 Top 10 Products By Quantity")
        plt.xlabel("Products")
        plt.ylabel("Total Quantity")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig(r"Output\charts\top_best_selling_products_by_quantity.png", dpi=300, bbox_inches='tight')
        plt.show()

    def _top_products_by_total_amount(self):
        top_products = (
            self.online_retail.groupby("Description")["TotalAmount"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )
        print("\n--------------- 💵 Top 10 Products by Total Sales Amount 💵 ---------------")
        print(top_products)
        print("-----------------------------------------------------------------------------\n")

        plt.figure(figsize=(10, 8))
        plt.bar(x=top_products.index, height=top_products.values, color="orange")
        plt.title("💵 Top 10 Products By Total Sales Amount")
        plt.xlabel("Products")
        plt.ylabel("Total Sales Amount")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig(r"Output\charts\top_products_by_total_amount.png", dpi=300, bbox_inches='tight')
        plt.show()

    def _top_products_by_unit_price(self):
        top_products = (
            self.online_retail.groupby("Description")["UnitPrice"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )
        print("\n--------------- 💎 Top 10 Products by Highest Unit Price 💎 ---------------")
        print(top_products)
        print("--------------------------------------------------------------------------\n")

        plt.figure(figsize=(12, 6))
        plt.bar(top_products.index, top_products.values)
        plt.title("💎 Top 10 Products by Maximum UnitPrice")
        plt.xlabel("Product Description")
        plt.ylabel("Total UnitPrice")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig(r"Output\charts\top_products_by_unit_price.png", dpi=300, bbox_inches='tight')
        plt.show()

    def _uk_most_sold_items(self):
        top_uk_items = (
            self.online_retail[self.online_retail.Country == "United Kingdom"]
            .groupby("Description")["Quantity"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )
        print("\n--------------- 🇬🇧 Most Frequently Sold Items in the UK 🇬🇧 ---------------")
        print(top_uk_items)
        print("-------------------------------------------------------------------------\n")

        plt.figure(figsize=(10, 8))
        plt.bar(x=top_uk_items.index, height=top_uk_items.values, color="green")
        plt.title("🇬🇧 Most Sold Items in The United Kingdom")
        plt.xlabel("Products")
        plt.ylabel("Quantity")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig(r"Output\charts\uk_most_sold_items.png", dpi=300, bbox_inches='tight')
        plt.show()

    def _uk_top_products_by_amount(self):
        top_uk_amount = (
            self.online_retail[self.online_retail.Country == "United Kingdom"]
            .groupby("Description")["TotalAmount"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )
        print("\n--------------- 🇬🇧 Top 10 Products by Total Sales in the UK 🇬🇧 ---------------")
        print(top_uk_amount)
        print("---------------------------------------------------------------------------\n")

        plt.figure(figsize=(10, 8))
        plt.bar(x=top_uk_amount.index, height=top_uk_amount.values, color="blue")
        plt.title("🇬🇧 Top 10 Products by Total Sales in the United Kingdom")
        plt.xlabel("Products")
        plt.ylabel("Total Sales Amount")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig(r"Output\charts\top_10_products_by_total_sales_in_the_united_kingdom.png", dpi=300, bbox_inches='tight')
        plt.show()

    def _top_customers_by_items_and_cost(self):
        top_customers = (
            self.online_retail.groupby("CustomerID")[["Quantity","TotalAmount"]]
            .sum()
            .sort_values(by=["Quantity","TotalAmount"], ascending=False)
            .head(10)
        )
        print("\n--------------- 👑 Top 10 Customers by Items & Total Cost 👑 ---------------")
        print(top_customers)
        print("----------------------------------------------------------------------------\n")

        plt.figure(figsize=(12, 8))
        plt.bar(x=top_customers.index.astype(str), height=top_customers["TotalAmount"], color="green", label="Total Amount")
        plt.bar(x=top_customers.index.astype(str), height=top_customers["Quantity"], color="blue", label="Quantity")
        plt.title("👑 Top 10 Customers by Purchased Items and Total Cost")
        plt.xlabel("Customer ID")
        plt.ylabel("Purchase Metrics")
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig(r"Output\charts\top_10_Customers_by_Purchased_Items_and_Total_Cost.png", dpi=300, bbox_inches='tight')
        plt.show()

    def _top_countries_by_users(self):
        top_users = self.online_retail["Country"].value_counts().head(10)
        print("\n--------------- 🎯 Number of Users 🎯 ---------------")
        print(top_users)
        print("-----------------------------------------------------\n")

        plt.figure(figsize=(10, 5))
        plt.barh(top_users.index, top_users.values, color="green")
        plt.title("🌐 Number of Users in Each Country")
        plt.xlabel("Number of Users (log scale)")
        plt.xscale("log")
        plt.ylabel("Country")
        plt.tight_layout()
        plt.savefig(r"Output\charts\top_10_Countries_by_Number_of_Users.png", dpi=300, bbox_inches='tight')
        plt.show()

    def _average_sales_per_country(self):
        avg_sales = self.online_retail.groupby("Country")["TotalAmount"].mean().sort_values(ascending=False)
        print("\n--------------- 📈 Average Sales per Country 📈 ---------------")
        print(avg_sales)
        print("---------------------------------------------------------------\n")

        plt.figure(figsize=(20, 8))
        plt.bar(avg_sales.index, avg_sales.values, color="seagreen")
        plt.title("📈 Average Sales of Each Country", fontsize=18, fontweight="bold")
        plt.xlabel("Country", fontsize=14)
        plt.ylabel("Average Sales", fontsize=14)
        plt.xticks(rotation=90, ha="right", fontsize=12)
        plt.yticks(fontsize=12)
        plt.grid(axis="y", linestyle="--", alpha=0.7)
        plt.tight_layout()
        plt.savefig(r"Output\charts\average_sales_per_country.png", dpi=300, bbox_inches='tight')
        plt.show()

    def _top_customers_buying_frequently(self):
        frequent_buyers = self.online_retail["CustomerID"].value_counts().head(10)
        print("\n--------------- 🛒 Top 10 Frequent Buyers 🛒 ---------------")
        print(frequent_buyers)
        print("----------------------------------------------------------\n")

        plt.figure(figsize=(10, 5))
        plt.bar(frequent_buyers.index.astype(str), frequent_buyers.values, color="green")
        plt.title("🛒 Top 10 Customers Who Buy Most Frequently")
        plt.xlabel("Customer ID")
        plt.ylabel("Number of Purchases")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig(r"Output\charts\top_10_Customers_Who_Buy_Most_Frequently.png", dpi=300, bbox_inches='tight')
        plt.show()

    def _recently_active_customers(self):
        analysis_date = self.online_retail["InvoiceDate"].max() + pd.Timedelta(days=1)
        recently = self.online_retail.groupby("CustomerID")["InvoiceDate"].max().apply(lambda x: (analysis_date - pd.to_datetime(x)).days)
        recently_df = recently.reset_index()
        recently_df.columns = ["CustomerID", "DaysSinceLastPurchase"]
        recently_df_sorted_top = recently_df.sort_values(by="DaysSinceLastPurchase").head(100)

        print("\n--------------- ⏱️ Top 100 Recently Active Customers ⏱️ ---------------")
        recently_df_sorted_top["DaysSinceLastPurchase"] = recently_df_sorted_top["DaysSinceLastPurchase"].astype(str) + " day(s) ago"
        print(recently_df_sorted_top)
        print("--------------------------------------------------------------------------\n")

    def _monthly_sales_trends(self):
        self.online_retail = self.online_retail.assign(
            YearMonth=self.online_retail["InvoiceDate"].dt.to_period("M")
        )
        monthly_sales = self.online_retail.groupby("YearMonth")["TotalAmount"].sum()
        print("\n--------------- 📅 Monthly Sales Trends (Dec-2010 to Dec-2011) 📅 ---------------")
        print(monthly_sales)
        print("------------------------------------------------------------\n")

        plt.figure(figsize=(10, 8))
        monthly_sales.plot(kind="line", marker="o")
        plt.title("📅 Monthly Sales Trends Dec-2010 to Dec-2011")
        plt.xlabel("Months")
        plt.ylabel("Total Sales (₹)")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(r"Output\charts\Monthly Sales Trends Dec-2010 to Dec-2011.png", dpi=300, bbox_inches='tight')
        plt.show()

    def _weekly_sales_trends(self):
        self.online_retail["Week"] = self.online_retail.InvoiceDate.dt.isocalendar().week
        weekly_sales_trends = (
            self.online_retail.groupby(["YearMonth", "Week"])["TotalAmount"]
            .sum()
            .reset_index()
        )
        weekly_sales_trends["YearMonth"] = weekly_sales_trends["YearMonth"].dt.strftime("%Y-M%m") + " W" + weekly_sales_trends["Week"].astype(str)
        print("\n--------------- 📅 Weekly Sales Trends 📅 ---------------")
        print(weekly_sales_trends)
        print("------------------------------------------------------------\n")

        plt.figure(figsize=(20, 10))
        plt.plot(
            weekly_sales_trends["YearMonth"], weekly_sales_trends["TotalAmount"],
            marker="o", linestyle="-", color="green"
        )
        plt.title("📅 Weekly Sales Trends")
        plt.xlabel("Year & Month")
        plt.ylabel("Sales ($)")
        plt.xticks(rotation=90, ha="right")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(r"Output\charts\weekly_sales_trends.png", dpi=300, bbox_inches='tight')
        plt.show()

    def _weekly_and_monthly_means(self):
        weekly_mean = self.online_retail.groupby(["YearMonth", "Week"])["TotalAmount"].sum().mean().round(2)
        monthly_mean = self.online_retail.groupby("YearMonth")["TotalAmount"].sum().mean().round(2)

        print("\n--------------- 📊 Weekly Sales Mean 📊 ---------------")
        print(f"Weekly Sales Mean: {weekly_mean}")
        print("-----------------------------------------------------\n")

        print("\n--------------- 📊 Monthly Sales Mean 📊 ---------------")
        print(f"Monthly Sales Mean: {monthly_mean}")
        print("------------------------------------------------------\n")

    def _max_sales_timeframes(self):
        monthly_max = self.online_retail.groupby("YearMonth")["TotalAmount"].sum().sort_values(ascending=False)
        daily_max = self.online_retail.groupby(self.online_retail["InvoiceDate"].dt.date)["TotalAmount"].sum().sort_values(ascending=False)
        weekly_max = self.online_retail.groupby(["YearMonth", "Week"])["TotalAmount"].sum().sort_values(ascending=False).reset_index()

        print("\n--------------- 📆 Month with Maximum Sales 📆 ---------------")
        print(f"Month: {monthly_max.index[0]}, Total Amount: {monthly_max.iloc[0]:,.2f}")
        print("---------------------------------------------------------------\n")

        print("\n--------------- 📅 Day with Maximum Sales 📅 ---------------")
        print(f"Day: {daily_max.index[0]}, Total Amount: {daily_max.iloc[0]:,.2f}")
        print("---------------------------------------------------------------\n")

        print("\n--------------- 🗓️ Week with Maximum Sales 🗓️ ---------------")
        print(f"Month: {weekly_max['YearMonth'].iloc[0]}, Week: {weekly_max['Week'].iloc[0]}, Total Amount: {weekly_max['TotalAmount'].iloc[0]:,.2f}")
        print("---------------------------------------------------------------\n")
        labels = [
        f"Month: {monthly_max.index[0]}", 
        f"Week: {weekly_max['YearMonth'].iloc[0]} W{weekly_max['Week'].iloc[0]}", 
        f"Day: {daily_max.index[0]}"
        ]
        values = [
            monthly_max.iloc[0],
            weekly_max['TotalAmount'].iloc[0],
            daily_max.iloc[0]
        ]

        plt.figure(figsize=(8, 6))
        plt.bar(labels, values, color=["skyblue", "orange", "green"])
        plt.ylabel("Total Sales")
        plt.title("📊 Maximum Sales: Month, Week, and Day")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig(r"Output\charts\max_sales_timeframes.png", dpi=300, bbox_inches='tight')
        plt.show()