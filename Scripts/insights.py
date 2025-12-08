import Scripts.eda

class RetailInsights:

    def __init__(self, online_retail):
        self.online_retail = online_retail

    def top_country_height_sales(self):
        top_country = (
            self.online_retail.groupby("Country")["TotalAmount"]
            .sum()
            .idxmax()
        )
        print(f"The country with the highest sales amount is: {top_country}")

    def top_best_selling_product(self):
        top_product = (
            self.online_retail.groupby("Description")["Quantity"]
            .sum()
            .idxmax()
        )
        print(f"The best-selling product is: {top_product}")

    def top_product_by_revenue(self):
        top_revenue_product = (
            self.online_retail.groupby("Description")["TotalAmount"]
            .sum()
            .idxmax()
        )
        print(f"The product generating the highest revenue is: {top_revenue_product}")

    def top_product_price(self):
        top_price_product = (
            self.online_retail.groupby("Description")["UnitPrice"]
            .sum()
            .idxmax()
        )
        print(f"The product with the highest price is: {top_price_product}")

    def top_item_in_each_country(self):
        print("Top item in each country:")
        for country in self.online_retail["Country"].unique():
            top_items = (
            self.online_retail[self.online_retail["Country"] == country]
                .groupby("Description")["Quantity"]
                .sum()
                .idxmax()
            )
            quantity_sold =(self.online_retail[self.online_retail["Country"] == country]
                    .groupby("Description")["Quantity"]
                    .sum()
                    .max()
                    )
            print(f"In {country}, the top item is: {top_items} with quantity {quantity_sold}")
    def top_uk_most_sold_items(self):
        top_uk_items = (
            self.online_retail[self.online_retail.Country == "United Kingdom"]
            .groupby("Description")["Quantity"]
            .sum()
            .idxmax()
        )
        print(f"The most sold items in the UK are: {top_uk_items}")

    def top_uk_product_by_amount(self):
        top_uk_amount = (
            self.online_retail[self.online_retail.Country == "United Kingdom"]
            .groupby("Description")["TotalAmount"]
            .sum()
            .idxmax()
        )
        print(f"The top products in the UK by sales amount are:\n{top_uk_amount}")

    def _top_customer_by_items_and_cost(self):
        grouped = (
            self.online_retail.groupby("CustomerID")[["Quantity", "TotalAmount"]]
            .sum()
            .sort_values(by=["Quantity", "TotalAmount"], ascending=False)
            .reset_index()
        )
        print(
            f"Top Customer: {grouped.iloc[0, 0]} — "
            f"Items Bought: {grouped.iloc[0, 1]}, "
            f"Total Spent: {grouped.iloc[0, 2]}"
        )
 
    def _top_country_by_users(self):
        top_user = self.online_retail["Country"].value_counts().idxmax()
        print(f"top country own the customers {top_user}")
    
    def  top_country_average_sales(self):
        avg_sales = self.online_retail.groupby("Country")["TotalAmount"].mean().idxmax()
        print(f"The country with the highest average sales is: {avg_sales}")
    
    def _top_customer_buying_frequently(self):
        frequent_buyers = self.online_retail["CustomerID"].value_counts().idxmax()
        print(f"Top frequently buyer {frequent_buyers}")
    
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