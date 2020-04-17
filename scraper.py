# scraper.py
#

import requests
from bs4 import BeautifulSoup
import pandas as pd
import html5lib
import numpy


class Team:
    def __init__(self, name, home):
        self.name = name
        # should be dict with keys of stadium_name, location (City, State/Prov), capacity
        self.home = home

        self.attendance = pd.Series(dtype=object)
        self.payroll = pd.Series(dtype=object)
        self.standings = pd.DataFrame(
            columns=["year", "win", "loss", "pct"]
        )

    def update_attendance(self, year, n_attendees):
        self.attendance[year] = n_attendees

    def update_payroll(self, year, amt_payroll):
        self.attendance[year] = amt_payroll

    def update_standings(self, year, data):
        self.attendance[year] = data

    def update_standings(self, data):
        self.standings.append(
            ignore_index=True,
            data=data
        )



mh = Team("Miami Heat",
          {"Arena": "AmericanAirlines Arena",
           "City": "Miami",
           "State/Province": "Florida",
           "Capacity": 19600})

if __name__ == '__main__':

    base_URL = "http://www.espn.com/nba/attendance/_/year/"
    domain_years = range(2020, 1998, -1)


    for i in domain_years:
        URL = base_URL + str(i)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html5lib')

        df = pd.read_html(URL, header=1).pop()  # to unpack table returned by this method

        year = soup.title.string.split().pop(0)
        avg_attendees = df.query('TEAM == "Heat"')['AVG'].item()

        mh.update_attendance(year, avg_attendees)


    print(mh.attendance)



# res = soup.find("table")
# table = res
# print(res.prettify())

# col_results = soup.find("table")
# cols = [col.text for col in col_results]
# print(cols)










