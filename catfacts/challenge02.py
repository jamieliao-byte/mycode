#!/usr/bin/env python3

'''API to dataframe '''

import requests, pandas as pd

def main():
    #read from API
    # conver to excel
    j = pd.read_json("http://api.tvmaze.com/search/shows?q=golden%20girls")
    j.to_excel('/home/student/static/movie_data.xls')

if __name__ == "__main__":
    main()

