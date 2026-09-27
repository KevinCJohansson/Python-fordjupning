import pandas as pd

def compute_metrics(df: pd.DataFrame) -> dict:
    top_products = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    return {
        "total_sales": df["Sales"].sum(),
        "n_orders": df["Order ID"].nunique(),
        "avg_order_value": df.groupby("Order ID")["Sales"].sum().mean(),
        "top_products": top_products,
        "start_date": df["Order Date"].min(),
        "end_date": df["Order Date"].max(),
    }