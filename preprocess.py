import pandas as pd
import os

# load walmart data
df = pd.read_csv("Walmart.csv")

os.makedirs("data", exist_ok=True)

# ---------- STORE TABLE ----------
store_df = df[["Store"]].drop_duplicates().copy()
store_df["StoreName"] = "Store_" + store_df["Store"].astype(str)
store_df["Region"] = "Region1"
store_df["OpenDate"] = "2010-01-01"
store_df.rename(columns={"Store": "StoreID"}, inplace=True)
store_df.to_csv("data/store.csv", index=False)

# ---------- DATE TABLE ----------
date_df = df[["Date"]].drop_duplicates().copy()
date_df["DateID"] = pd.to_datetime(date_df["Date"], format="%d-%m-%Y")
date_df["WeekStartDate"] = date_df["DateID"]
date_df["WeekOfYear"] = date_df["DateID"].dt.isocalendar().week
date_df["Month"] = date_df["DateID"].dt.month
date_df["Quarter"] = date_df["DateID"].dt.quarter
date_df["Year"] = date_df["DateID"].dt.year
date_df["IsHolidayWeek"] = False

date_df["DateID"] = date_df["DateID"].dt.strftime("%Y-%m-%d")
date_df["WeekStartDate"] = pd.to_datetime(date_df["WeekStartDate"]).dt.strftime("%Y-%m-%d")

date_df = date_df[[
    "DateID",
    "WeekStartDate",
    "WeekOfYear",
    "Month",
    "Quarter",
    "Year",
    "IsHolidayWeek"
]]

date_df.to_csv("data/date_dim.csv", index=False)

# ---------- SALES FACT ----------
sales_df = df.copy()

sales_df.rename(columns={
    "Store": "StoreID",
    "Date": "DateID",
    "Weekly_Sales": "Weekly_Sales",
    "Holiday_Flag": "Holiday_Flag"
}, inplace=True)

sales_df["DateID"] = pd.to_datetime(sales_df["DateID"], format="%d-%m-%Y").dt.strftime("%Y-%m-%d")

sales_df = sales_df[[
    "StoreID",
    "DateID",
    "Weekly_Sales",
    "Holiday_Flag"
]]

sales_df.to_csv("data/sales_fact.csv", index=False)

# ---------- WEATHER ----------
weather_df = sales_df.copy()
weather_df["Temperature"] = 70
weather_df["WeatherSource"] = "NOAA"

weather_df = weather_df[[
    "StoreID",
    "DateID",
    "Temperature",
    "WeatherSource"
]]

weather_df.to_csv("data/weather.csv", index=False)

# ---------- ECONOMIC ----------
econ_df = sales_df.copy()
econ_df["Fuel_Price"] = 3.5
econ_df["CPI"] = 200
econ_df["Unemployment"] = 6

econ_df = econ_df[[
    "StoreID",
    "DateID",
    "Fuel_Price",
    "CPI",
    "Unemployment"
]]

econ_df.to_csv("data/economic.csv", index=False)

# ---------- HOLIDAY ----------
holiday_df = pd.DataFrame({
    "HolidayID": [1, 2],
    "HolidayName": ["Christmas", "Thanksgiving"],
    "HolidayType": ["Federal", "Federal"],
    "Notes": ["Holiday", "Holiday"]
})

holiday_df.to_csv("data/holiday.csv", index=False)

print("CSV files created in data folder")