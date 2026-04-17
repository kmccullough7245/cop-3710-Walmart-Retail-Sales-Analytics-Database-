import pandas as pd
import os

df = pd.read_csv("Walmart.csv")
df.columns = [c.strip() for c in df.columns]

df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")
df["Holiday_Flag"] = df["Holiday_Flag"].astype(int)

os.makedirs("data", exist_ok=True)

store_df = (
    df[["Store"]]
    .drop_duplicates()
    .sort_values("Store")
    .rename(columns={"Store": "StoreID"})
)

date_df = (
    df.groupby("Date", as_index=False)
      .agg(IsHolidayWeek=("Holiday_Flag", "max"))
      .copy()
)

date_df["DateID"] = date_df["Date"]
date_df["WeekStartDate"] = date_df["Date"]
date_df["WeekOfYear"] = date_df["Date"].dt.isocalendar().week.astype(int)
date_df["MonthNum"] = date_df["Date"].dt.month
date_df["QuarterNum"] = date_df["Date"].dt.quarter
date_df["YearNum"] = date_df["Date"].dt.year

date_df = date_df[
    ["DateID", "WeekStartDate", "WeekOfYear", "MonthNum", "QuarterNum", "YearNum", "IsHolidayWeek"]
].sort_values("DateID")

sales_df = (
    df[["Store", "Date", "Weekly_Sales", "Holiday_Flag"]]
    .copy()
    .rename(columns={
        "Store": "StoreID",
        "Date": "DateID"
    })
    .sort_values(["StoreID", "DateID"])
)

weather_df = (
    df[["Store", "Date", "Temperature"]]
    .copy()
    .rename(columns={
        "Store": "StoreID",
        "Date": "DateID"
    })
    .sort_values(["StoreID", "DateID"])
)

economic_df = (
    df[["Store", "Date", "Fuel_Price", "CPI", "Unemployment"]]
    .copy()
    .rename(columns={
        "Store": "StoreID",
        "Date": "DateID"
    })
    .sort_values(["StoreID", "DateID"])
)

for out_df in [date_df, sales_df, weather_df, economic_df]:
    for col in out_df.columns:
        if pd.api.types.is_datetime64_any_dtype(out_df[col]):
            out_df[col] = out_df[col].dt.strftime("%Y-%m-%d")

store_df.to_csv("store.csv", index=False)
date_df.to_csv("date_dim.csv", index=False)
sales_df.to_csv("sales_fact.csv", index=False)
weather_df.to_csv("weather.csv", index=False)
economic_df.to_csv("economic.csv", index=False)

store_df.to_csv("data/store.csv", index=False)
date_df.to_csv("data/date_dim.csv", index=False)
sales_df.to_csv("data/sales_fact.csv", index=False)
weather_df.to_csv("data/weather.csv", index=False)
economic_df.to_csv("data/economic.csv", index=False)

print("Clean CSV files created successfully.")
print(f"Store rows: {len(store_df)}")
print(f"Date rows: {len(date_df)}")
print(f"Sales rows: {len(sales_df)}")
print(f"Weather rows: {len(weather_df)}")
print(f"Economic rows: {len(economic_df)}")
