"""
Walmart Sales Analytics Application

This application connects to the Walmart database and provides
five user-facing features for viewing and analyzing sales data.

Before running:
- update Oracle credentials
- update the Instant Client path if needed
"""




import oracledb

# ---------------------------------
# DATABASE CONFIGURATION
# Replace these with your teammate's Oracle credentials
# ---------------------------------
DB_USER = "YOUR_USERNAME"
DB_PASS = "YOUR_PASSWORD"
DB_DSN = "YOUR_HOST:PORT/SERVICE_NAME"

LIB_DIR = r"PATH_TO_ORACLE_INSTANT_CLIENT"

oracledb.init_oracle_client(lib_dir=LIB_DIR)


def connect_db():
    return oracledb.connect(
        user=DB_USER,
        password=DB_PASS,
        dsn=DB_DSN
    )


def print_rows(cursor, rows):
    """
    Prints query results in a readable table-like format.
    """
    if not rows:
        print("\nNo results found.\n")
        return

    headers = [col[0] for col in cursor.description]
    widths = [len(h) for h in headers]

    for row in rows:
        for i, value in enumerate(row):
            widths[i] = max(widths[i], len(str(value)))

    header_line = " | ".join(headers[i].ljust(widths[i]) for i in range(len(headers)))
    separator = "-+-".join("-" * widths[i] for i in range(len(headers)))

    print()
    print(header_line)
    print(separator)

    for row in rows:
        print(" | ".join(str(row[i]).ljust(widths[i]) for i in range(len(row))))
    print()


def feature_1_weekly_sales_by_store(cursor):
    """
    1. View weekly sales for a store in a date range
    Uses JOIN between Sales_Fact and Date_Dim
    """
    store_id = input("Enter Store ID: ").strip()
    start_date = input("Enter start date (YYYY-MM-DD): ").strip()
    end_date = input("Enter end date (YYYY-MM-DD): ").strip()

    sql = """
        SELECT sf.StoreID,
               dd.DateID,
               sf.Weekly_Sales
        FROM Sales_Fact sf
        JOIN Date_Dim dd
          ON sf.DateID = dd.DateID
        WHERE sf.StoreID = :1
          AND dd.DateID BETWEEN TO_DATE(:2, 'YYYY-MM-DD')
                            AND TO_DATE(:3, 'YYYY-MM-DD')
        ORDER BY dd.DateID
    """

    cursor.execute(sql, [store_id, start_date, end_date])
    rows = cursor.fetchall()
    print_rows(cursor, rows)


def feature_2_holiday_week_sales(cursor):
    """
    2. Show all holiday week sales with store number
    Uses JOIN between Sales_Fact and Date_Dim
    """
    sql = """
        SELECT sf.StoreID,
               dd.DateID,
               sf.Weekly_Sales
        FROM Sales_Fact sf
        JOIN Date_Dim dd
          ON sf.DateID = dd.DateID
        WHERE sf.Holiday_Flag = 1
        ORDER BY dd.DateID, sf.StoreID
    """

    cursor.execute(sql)
    rows = cursor.fetchall()
    print_rows(cursor, rows)


def feature_3_avg_sales_with_economic_conditions(cursor):
    """
    3. Show average sales with economic conditions for a selected store
    Uses JOIN between Sales_Fact, Economic_Observation, and Store
    """
    store_id = input("Enter Store ID: ").strip()

    sql = """
        SELECT s.StoreID,
               s.StoreName,
               ROUND(AVG(sf.Weekly_Sales), 2) AS Avg_Weekly_Sales,
               ROUND(AVG(eo.Fuel_Price), 2) AS Avg_Fuel_Price,
               ROUND(AVG(eo.CPI), 2) AS Avg_CPI,
               ROUND(AVG(eo.Unemployment), 2) AS Avg_Unemployment
        FROM Store s
        JOIN Sales_Fact sf
          ON s.StoreID = sf.StoreID
        JOIN Economic_Observation eo
          ON sf.StoreID = eo.StoreID
         AND sf.DateID = eo.DateID
        WHERE s.StoreID = :1
        GROUP BY s.StoreID, s.StoreName
    """

    cursor.execute(sql, [store_id])
    rows = cursor.fetchall()
    print_rows(cursor, rows)


def feature_4_top_stores_by_total_sales(cursor):
    """
    4. Show top stores by total sales in a date range
    Uses JOIN between Sales_Fact, Date_Dim, and Store
    """
    start_date = input("Enter start date (YYYY-MM-DD): ").strip()
    end_date = input("Enter end date (YYYY-MM-DD): ").strip()

    sql = """
        SELECT s.StoreID,
               s.StoreName,
               ROUND(SUM(sf.Weekly_Sales), 2) AS Total_Sales
        FROM Store s
        JOIN Sales_Fact sf
          ON s.StoreID = sf.StoreID
        JOIN Date_Dim dd
          ON sf.DateID = dd.DateID
        WHERE dd.DateID BETWEEN TO_DATE(:1, 'YYYY-MM-DD')
                            AND TO_DATE(:2, 'YYYY-MM-DD')
        GROUP BY s.StoreID, s.StoreName
        ORDER BY Total_Sales DESC
        FETCH FIRST 10 ROWS ONLY
    """

    cursor.execute(sql, [start_date, end_date])
    rows = cursor.fetchall()
    print_rows(cursor, rows)


def feature_5_compare_holiday_vs_nonholiday_avg_sales(cursor):
    """
    5. Compare average sales on holiday vs non-holiday weeks
    Uses Sales_Fact only (or can be extended to join Date_Dim if needed)
    """
    sql = """
        SELECT CASE
                   WHEN Holiday_Flag = 1 THEN 'Holiday Week'
                   ELSE 'Non-Holiday Week'
               END AS Week_Type,
               ROUND(AVG(Weekly_Sales), 2) AS Avg_Weekly_Sales
        FROM Sales_Fact
        GROUP BY Holiday_Flag
        ORDER BY Week_Type
    """

    cursor.execute(sql)
    rows = cursor.fetchall()
    print_rows(cursor, rows)


def show_menu():
    print("==============================================")
    print(" Walmart Sales Analytics Application")
    print("==============================================")
    print("1. View weekly sales for a store in a date range")
    print("2. Show all holiday week sales with store number")
    print("3. Show average sales with economic conditions for a selected store")
    print("4. Show top stores by total sales in a date range")
    print("5. Compare average sales on holiday vs non-holiday weeks")
    print("6. Exit")
    print("==============================================")


def main():
    conn = None
    cursor = None

    try:
        print("Connecting to Oracle database...")
        conn = connect_db()
        cursor = conn.cursor()
        print("Connected successfully.\n")

        while True:
            show_menu()
            choice = input("Enter your choice (1-6): ").strip()

            if choice == "1":
                feature_1_weekly_sales_by_store(cursor)
            elif choice == "2":
                feature_2_holiday_week_sales(cursor)
            elif choice == "3":
                feature_3_avg_sales_with_economic_conditions(cursor)
            elif choice == "4":
                feature_4_top_stores_by_total_sales(cursor)
            elif choice == "5":
                feature_5_compare_holiday_vs_nonholiday_avg_sales(cursor)
            elif choice == "6":
                print("Exiting application.")
                break
            else:
                print("\nInvalid choice. Please select a number from 1 to 6.\n")

    except Exception as e:
        print("\nAn error occurred:")
        print(e)

    finally:
        try:
            if cursor is not None:
                cursor.close()
        except Exception:
            pass

        try:
            if conn is not None:
                conn.close()
        except Exception:
            pass

        print("Database connection closed.")


if __name__ == "__main__":
    main()


