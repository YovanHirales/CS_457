import requests
import csv
from bs4 import BeautifulSoup

def main():
    r = requests.get("https://www.unr.edu/admissions/records/academic-calendar/finals-schedule")
    soup = BeautifulSoup(r.text, 'html.parser')
    print(r.text)
    # print(soup.get_text())

main()