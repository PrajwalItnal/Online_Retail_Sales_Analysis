class RetailInsights:

    def __init__(self, online_retail):
        self.online_retail = online_retail

    def generate_insights(self):
        print("\n" + "="*80)
        print("📊 ONLINE RETAIL — EXPLORATORY INSIGHTS REPORT 📊")
        print("="*80)

        self.top_country_height_sales()
        self.top_best_selling_product()
        self.top_product_by_revenue()
        self.top_product_price()
        self.top_item_in_each_country()
        self.top_uk_most_sold_items()
        self.top_uk_product_by_amount()
        self._top_customer_by_items_and_cost()
        self._top_country_by_users()
        self.top_country_average_sales()
        self._top_customer_buying_frequently()
        self._max_sales_timeframes()

        print("="*80)
        print("📘 END OF AUTOMATED INSIGHTS REPORT 📘")
        print("="*80)

    # -------------------- Country & Product Insights --------------------
    def top_country_height_sales(self):
        top_country = self.online_retail.groupby("Country")["TotalAmount"].sum().idxmax()
        print("\n--------------- 🌍 Top Country by Total Sales ---------------")
        print(f"Country: {top_country}")
        print("---------------------------------------------------------------\n")

    def top_best_selling_product(self):
        top_product = self.online_retail.groupby("Description")["Quantity"].sum().idxmax()
        print("\n--------------- 🛒 Best-Selling Product (Highest Quantity Sold) ---------------")
        print(f"Product: {top_product}")
        print("---------------------------------------------------------------\n")

    def top_product_by_revenue(self):
        top_revenue_product = self.online_retail.groupby("Description")["TotalAmount"].sum().idxmax()
        print("\n--------------- 💰 Top Product by Revenue ---------------")
        print(f"Product: {top_revenue_product}")
        print("---------------------------------------------------------------\n")

    def top_product_price(self):
        top_price_product = self.online_retail.groupby("Description")["UnitPrice"].sum().idxmax()
        print("\n--------------- 💎 Product With Highest Price ---------------")
        print(f"Product: {top_price_product}")
        print("---------------------------------------------------------------\n")

    def top_item_in_each_country(self):
        print("\n--------------- 🏅 Top Item in Each Country ---------------")
        for country in self.online_retail["Country"].unique():
            country_data = self.online_retail[self.online_retail["Country"] == country]
            top_item = country_data.groupby("Description")["Quantity"].sum().idxmax()
            qty_sold = country_data.groupby("Description")["Quantity"].sum().max()
            print(f"{country}: {top_item}, Quantity Sold: {qty_sold}")
        print("---------------------------------------------------------------\n")

    def top_uk_most_sold_items(self):
        uk_data = self.online_retail[self.online_retail["Country"] == "United Kingdom"]
        top_item = uk_data.groupby("Description")["Quantity"].sum().idxmax()
        print("\n--------------- 🇬🇧 UK Market — Most Sold Item ---------------")
        print(f"Product: {top_item}")
        print("---------------------------------------------------------------\n")

    def top_uk_product_by_amount(self):
        uk_data = self.online_retail[self.online_retail["Country"] == "United Kingdom"]
        top_item = uk_data.groupby("Description")["TotalAmount"].sum().idxmax()
        print("\n--------------- 🇬🇧 UK Market — Top Product by Amount ---------------")
        print(f"Product: {top_item}")
        print("---------------------------------------------------------------\n")

    # -------------------- Customer Insights --------------------
    def _top_customer_by_items_and_cost(self):
        grouped = (
            self.online_retail.groupby("CustomerID")[["Quantity", "TotalAmount"]]
            .sum()
            .sort_values(by=["Quantity", "TotalAmount"], ascending=False)
            .reset_index()
        )
        print("\n--------------- 👤 Top Customer by Items & Spending ---------------")
        print(f"CustomerID: {grouped.iloc[0, 0]}, Items Bought: {grouped.iloc[0, 1]}, Total Spent: £{grouped.iloc[0, 2]:,.2f}")
        print("---------------------------------------------------------------\n")

    def _top_country_by_users(self):
        top_user = self.online_retail["Country"].value_counts().idxmax()
        print("\n--------------- 🌍 Country With Most Customers ---------------")
        print(f"Country: {top_user}")
        print("---------------------------------------------------------------\n")

    def top_country_average_sales(self):
        avg_sales = self.online_retail.groupby("Country")["TotalAmount"].mean().idxmax()
        print("\n--------------- 📊 Top Country by Average Sales ---------------")
        print(f"Country: {avg_sales}")
        print("---------------------------------------------------------------\n")

    def _top_customer_buying_frequently(self):
        frequent_buyers = self.online_retail["CustomerID"].value_counts().idxmax()
        print("\n--------------- 🛍️ Most Frequent Customer ---------------")
        print(f"CustomerID: {frequent_buyers}")
        print("---------------------------------------------------------------\n")

    # -------------------- Sales Timeframes --------------------
    def _max_sales_timeframes(self):
        monthly_max = self.online_retail.groupby("YearMonth")["TotalAmount"].sum().sort_values(ascending=False)
        daily_max = self.online_retail.groupby(self.online_retail["InvoiceDate"].dt.date)["TotalAmount"].sum().sort_values(ascending=False)
        weekly_max = self.online_retail.groupby(["YearMonth", "Week"])["TotalAmount"].sum().sort_values(ascending=False).reset_index()

        print("\n--------------- 📆 Month with Maximum Sales 📆 ---------------")
        print(f"Month: {monthly_max.index[0]}, Total Amount: £{monthly_max.iloc[0]:,.2f}")
        print("---------------------------------------------------------------\n")

        print("\n--------------- 📅 Day with Maximum Sales 📅 ---------------")
        print(f"Day: {daily_max.index[0]}, Total Amount: £{daily_max.iloc[0]:,.2f}")
        print("---------------------------------------------------------------\n")

        print("\n--------------- 🗓️ Week with Maximum Sales 🗓️ ---------------")
        print(f"Month: {weekly_max['YearMonth'].iloc[0]}, Week: {weekly_max['Week'].iloc[0]}, Total Amount: £{weekly_max['TotalAmount'].iloc[0]:,.2f}")
        print("---------------------------------------------------------------\n")
