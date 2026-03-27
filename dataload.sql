-- STORE
INSERT INTO Store VALUES (1, 'Store_1', 'Region1', DATE '2010-01-01');
INSERT INTO Store VALUES (2, 'Store_2', 'Region1', DATE '2010-01-01');
INSERT INTO Store VALUES (3, 'Store_3', 'Region1', DATE '2010-01-01');


-- DATE_DIM
INSERT INTO Date_Dim VALUES (
    DATE '2010-02-05',
    DATE '2010-02-05',
    5,
    2,
    1,
    2010,
    0
);

INSERT INTO Date_Dim VALUES (
    DATE '2010-02-12',
    DATE '2010-02-12',
    6,
    2,
    1,
    2010,
    0
);


-- SALES_FACT
INSERT INTO Sales_Fact VALUES (
    1,
    DATE '2010-02-05',
    24924.50,
    0
);

INSERT INTO Sales_Fact VALUES (
    1,
    DATE '2010-02-12',
    46039.49,
    1
);


-- WEATHER
INSERT INTO Weather_Observation VALUES (
    1,
    DATE '2010-02-05',
    70,
    'NOAA'
);

INSERT INTO Weather_Observation VALUES (
    1,
    DATE '2010-02-12',
    65,
    'NOAA'
);


-- ECONOMIC
INSERT INTO Economic_Observation VALUES (
    1,
    DATE '2010-02-05',
    3.5,
    200,
    6
);

INSERT INTO Economic_Observation VALUES (
    1,
    DATE '2010-02-12',
    3.6,
    201,
    6.1
);


-- HOLIDAY
INSERT INTO Holiday VALUES (
    1,
    'Christmas',
    'Federal',
    'Holiday'
);

INSERT INTO Holiday VALUES (
    2,
    'Thanksgiving',
    'Federal',
    'Holiday'
);
