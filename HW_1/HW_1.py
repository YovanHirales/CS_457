import requests
import csv
from bs4 import BeautifulSoup

def main():
    # Grab HTML from URL
    # URL from UNR's website - https://www.unr.edu/admissions/records/academic-calendar/finals-schedule
    r = requests.get("https://www.unr.edu/admissions/records/academic-calendar/finals-schedule")
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # Add headers to first row
    headers = ['Day of Week']
    for header in soup.find_all('th')[:3]:
        headers.append(str(header.get_text()))

    schedule = [headers]

    # Loop over each table and add rows to csv
    for table in soup.find_all('table'):
        # Grab table rows
        for tr in table.find_all('tr')[1:]:
            # Grab Day of Week
            dayOfWeek = table.find_previous('h2')
            row = [str(dayOfWeek.get_text())]

            # Grab row data
            for td in tr.find_all('td'):
                # Add data to row
                row.append(str(td.get_text()).replace("\xa0", " "))
            # Add row to schedule
            schedule.append(row)
    
    # Write schedule to csv
    with open('schedule.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(schedule)

            


main()