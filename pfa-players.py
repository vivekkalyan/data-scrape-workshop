import requests
from bs4 import BeautifulSoup

urls = [
    "https://en.wikipedia.org/wiki/PFA_Team_of_the_Year_(1960s)",
    "https://en.wikipedia.org/wiki/PFA_Team_of_the_Year_(1970s)",
    "https://en.wikipedia.org/wiki/PFA_Team_of_the_Year_(1980s)",
    "https://en.wikipedia.org/wiki/PFA_Team_of_the_Year_(1990s)",
    "https://en.wikipedia.org/wiki/PFA_Team_of_the_Year_(2000s)",
    "https://en.wikipedia.org/wiki/PFA_Team_of_the_Year_(2010s)"
]

res = requests.get("https://en.wikipedia.org/wiki/PFA_Team_of_the_Year_(2000s)")

assert(res.status_code == 200)

soup = BeautifulSoup(res.content)
h4s = soup.find_all("h4")
pl = []
for header in h4s:
    if "Premier League" in header.span.string:
        pl.append(header)

assert(len(pl)==10)
year=2000
for header in pl:
    print(year)
    year = year + 1
    table = header.find_next_sibling('table')
    for row in table.find_all('tr'):
        values = row.find_all('td')
        if len(values) == 0:
            continue
        player = row.find('th').a.string
        club = values[1]
        if values[1].a:
            club = values[1].a.string
        else:
            club = values[1].string
        club = club.strip('\n')

        if "Liverpool" in club:
            print(club, player)
