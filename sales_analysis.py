import pandas as pd 

class SalesAnalyzer:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = pd.read_csv(file_path)

    def analyze(self) -> dict:
        # Calculate revenue per order
        self.df["order_revenue"] = (
            self.df["quantity"]
            * self.df["unit_price"]
            * (1 - self.df["discount_percent"] / 100)
        )

        # Return structured metrics
        return {
            "total_revenue": round(self.df["order_revenue"].sum(), 2),
            "average_order_value": round(self.df["order_revenue"].mean(), 2),
            "orders": len(self.df),
            "revenue_by_category": (
                self.df.groupby("product_category")["order_revenue"]
                .sum()
                .round(2)
                .to_dict()
            ),
            "revenue_by_region": (
                self.df.groupby("region")["order_revenue"]
                .sum()
                .round(2)
                .to_dict()
            ),
            "top_payment_method": (
                self.df.groupby("payment_method")["order_revenue"]
                .sum()
                .idxmax()
            ),
        }