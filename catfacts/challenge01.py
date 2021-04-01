#!/usr/bin/env python3

'''API to dataframe '''

import requests, pandas as pd

def main():
    #read from API
    # conver to excel
    j = pd.read_json("https://api.census.gov/data.json")
    j.to_excel('/home/student/static/census_data.xls')

if __name__ == "__main__":
    main()

