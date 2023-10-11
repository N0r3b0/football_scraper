import requests
from bs4 import BeautifulSoup
import pandas as pd

premierLeagueTable = []

url = 'https://www.bbc.com/sport/football/tables'
response = requests.get(url)
print('Loading tables')
print(response.status_code)

html = response.text
soup = BeautifulSoup(html, 'html.parser')

allRows = soup.select('table tbody tr')
print('Going through rows')

for row in allRows:
    tds = row.find_all('td')
    team = tds[2].text.strip()
    played = tds[3].text.strip()
    won = tds[4].text.strip()
    drawn = tds[5].text.strip()
    lost = tds[6].text.strip()
    gf = tds[7].text.strip()
    against = tds[8].text.strip()
    gd = tds[9].text.strip()
    points = tds[10].text.strip()
    
    premierLeagueTable.append({
        'Team': team,
        'Played': played,
        'Won': won,
        'Drawn': drawn,
        'Lost': lost,
        'Goals For': gf,
        'Goals Against': against,
        'Goals Difference': gd,
        'Points': points
    })

print('Saving data to CSV')

df = pd.DataFrame(premierLeagueTable)
df.to_csv('footballData.csv', index=False)

print('Saved to csv')
