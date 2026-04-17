import pandas as pd

store = pd.read_csv("store.csv")
date_dim = pd.read_csv("date_dim.csv")
sales = pd.read_csv("sales_fact.csv")
weather = pd.read_csv("weather.csv")
economic = pd.read_csv("economic.csv")

lines = []

lines.append("-- Auto-generated from CSV files")
lines.append("-- Run create_db.sql first")
lines.append("")

for _, r in store.iterrows():
    lines.append(
        f"INSERT INTO Store (StoreID) VALUES ({int(r['StoreID'])});"
    )

for _, r in date_dim.iterrows():
    lines.append(
        "INSERT INTO Date_Dim "
        "(DateID, WeekStartDate, WeekOfYear, MonthNum, QuarterNum, YearNum, IsHolidayWeek) "
        f"VALUES (DATE '{r['DateID']}', DATE '{r['WeekStartDate']}', "
        f"{int(r['WeekOfYear'])}, {int(r['MonthNum'])}, {int(r['QuarterNum'])}, "
        f"{int(r['YearNum'])}, {int(r['IsHolidayWeek'])});"
    )

for _, r in sales.iterrows():
    lines.append(
        "INSERT INTO Sales_Fact "
        "(StoreID, DateID, Weekly_Sales, Holiday_Flag) "
        f"VALUES ({int(r['StoreID'])}, DATE '{r['DateID']}', "
        f"{float(r['Weekly_Sales']):.2f}, {int(r['Holiday_Flag'])});"
    )

for _, r in weather.iterrows():
    temp = "NULL" if pd.isna(r["Temperature"]) else f"{float(r['Temperature']):.2f}"
    lines.append(
        "INSERT INTO Weather_Observation "
        "(StoreID, DateID, Temperature) "
        f"VALUES ({int(r['StoreID'])}, DATE '{r['DateID']}', {temp});"
    )

for _, r in economic.iterrows():
    fuel = "NULL" if pd.isna(r["Fuel_Price"]) else f"{float(r['Fuel_Price']):.3f}"
    cpi = "NULL" if pd.isna(r["CPI"]) else f"{float(r['CPI']):.3f}"
    unemp = "NULL" if pd.isna(r["Unemployment"]) else f"{float(r['Unemployment']):.3f}"
    lines.append(
        "INSERT INTO Economic_Observation "
        "(StoreID, DateID, Fuel_Price, CPI, Unemployment) "
        f"VALUES ({int(r['StoreID'])}, DATE '{r['DateID']}', {fuel}, {cpi}, {unemp});"
    )

lines.append("COMMIT;")

with open("dataload.sql", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("dataload.sql generated from CSV files.")
