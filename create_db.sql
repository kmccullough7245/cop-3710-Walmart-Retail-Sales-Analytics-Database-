#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://aka.ms/MinecraftEULA).
#Fri Nov 28 17:24:24 EST 2025
eula=true




CREATE TABLE Store (
    StoreID INT PRIMARY KEY,
    StoreName VARCHAR(100),
    Region VARCHAR(50),
    OpenDate DATE
);

CREATE TABLE Store_Manager (
    StoreID INT,
    ManagerUserID INT,
    ManagerName VARCHAR(100),
    ManagerEmail VARCHAR(100),
    PRIMARY KEY (StoreID),
    FOREIGN KEY (StoreID) REFERENCES Store(StoreID)
);

CREATE TABLE Date_Dim (
    DateID DATE PRIMARY KEY,
    WeekStartDate DATE,
    WeekOfYear INT,
    Month INT,
    Quarter INT,
    Year INT,
    IsHolidayWeek BOOLEAN
);

CREATE TABLE Holiday (
    HolidayID INT PRIMARY KEY,
    HolidayName VARCHAR(100),
    HolidayType VARCHAR(50),
    Notes VARCHAR(200)
);

CREATE TABLE Date_Holiday (
    DateID DATE,
    HolidayID INT,
    PRIMARY KEY (DateID, HolidayID),
    FOREIGN KEY (DateID) REFERENCES Date_Dim(DateID),
    FOREIGN KEY (HolidayID) REFERENCES Holiday(HolidayID)
);

CREATE TABLE Sales_Fact (
    StoreID INT,
    DateID DATE,
    Weekly_Sales DECIMAL(10,2),
    Holiday_Flag BOOLEAN,
    PRIMARY KEY (StoreID, DateID),
    FOREIGN KEY (StoreID) REFERENCES Store(StoreID),
    FOREIGN KEY (DateID) REFERENCES Date_Dim(DateID)
);

CREATE TABLE Weather_Observation (
    StoreID INT,
    DateID DATE,
    Temperature DECIMAL(5,2),
    WeatherSource VARCHAR(50),
    PRIMARY KEY (StoreID, DateID),
    FOREIGN KEY (StoreID) REFERENCES Store(StoreID),
    FOREIGN KEY (DateID) REFERENCES Date_Dim(DateID)
);

CREATE TABLE Economic_Observation (
    StoreID INT,
    DateID DATE,
    Fuel_Price DECIMAL(5,2),
    CPI DECIMAL(6,2),
    Unemployment DECIMAL(4,2),
    PRIMARY KEY (StoreID, DateID),
    FOREIGN KEY (StoreID) REFERENCES Store(StoreID),
    FOREIGN KEY (DateID) REFERENCES Date_Dim(DateID)
);

CREATE TABLE Sales_Spike_Log (
    SpikeLogID INT PRIMARY KEY,
    StoreID INT,
    DateID DATE,
    Weekly_Sales DECIMAL(10,2),
    BaselineSales DECIMAL(10,2),
    SpikePercent DECIMAL(5,2),
    SpikeReason VARCHAR(100),
    CreatedAt TIMESTAMP,
    FOREIGN KEY (StoreID) REFERENCES Store(StoreID),
    FOREIGN KEY (DateID) REFERENCES Date_Dim(DateID)
);