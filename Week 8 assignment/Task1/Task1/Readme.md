# NYC Taxi Data Analysis with PySpark

## Overview

This project loads NYC taxi data into Databricks, processes it using PySpark, and performs a series of analytical queries. The data is sourced from the NYC Taxi and Limousine Commission's public dataset.

## Data Source

The data used in this analysis can be found at:
- [NYC Taxi Data](http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml Choose Trip sheet data -> 2018 -> January -> yellow type https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2020-01.csv)
- Direct download link for January 2020 Yellow Taxi data: [yellow_tripdata_2020-01.csv](https://drive.google.com/file/d/1za1q1PVdMIlBgUxtJSozvyK7calNj2cD/view?usp=drive_link)

## Requirements

- Databricks account
- Cluster configured with PySpark

## Steps to Execute

1. **Load Data to Databricks**: 
   - Open the Databricks workspace and create a new notebook.
   - Copy the script provided in the `notebook.py` file into your Databricks notebook.
   - Run each cell sequentially to load the data and execute the queries.

2. **Queries Performed**:
   - **Query 1**: Add a column named "Revenue" which is the sum of specific fare-related columns.
   - **Query 2**: Calculate the increasing count of total passengers in New York City by area.
   - **Query 3**: Compute the real-time average fare and total earnings amount earned by 2 vendors.
   - **Query 4**: Count the number of payments made by each payment mode.
   - **Query 5**: Identify the highest two gaining vendors on a particular date with the number of passengers and total distance traveled by cab.
   - **Query 6**: Determine the route between two locations with the most number of passengers.
   - **Query 7**: Get the top pickup locations with the most passengers in the last 5/10 seconds.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
