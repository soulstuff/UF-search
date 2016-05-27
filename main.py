import urllib
import urllib.request
from bs4 import BeautifulSoup
from collections import defaultdict


def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, 'html.parser')
    return soupdata


soup = make_soup('http://www.sii.cl/pagina/valores/uf/uf2016.htm')

data = []
table = soup.find('table', attrs={'class': "tabla"})
table_body = table.find('tbody')

rows = table_body.find_all('tr')

for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    # data.append([ele for ele in cols if ele])
    data.append(cols)
output = defaultdict(list)

for day in data:
    output["enero"].append(day[0])
    output["febrero"].append(day[1])
    output["marzo"].append(day[2])
    output["abril"].append(day[3])
    output["mayo"].append(day[4])
    output["junio"].append(day[5])
    output["julio"].append(day[6])
    output["agosto"].append(day[7])
    output["septiembre"].append(day[8])
    output["octubre"].append(day[9])
    output["noviembre"].append(day[10])
    output["diciembre"].append(day[11])

print(output["enero"])
