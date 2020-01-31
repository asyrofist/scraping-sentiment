# Importing the necessary libraries
import pandas as pd
import urllib
import bs4 as bs
import lxml
from urllib import request

# Specify the url
# wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
link_url = input("masukkan url anda: ")

#Query the website and return the html to the variable 'page'
page = urllib.request.urlopen(link_url)

#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = bs.BeautifulSoup(page, 'lxml')

# # Use function “prettify” to look at nested structure of HTML page
# print(soup.prettify())

# # tampilkan title
# print(soup.title)

# # tampilkan srtring dalam title
# print(soup.title.string)

# # Find all the links within page’s <a> tags
# print(soup.find_all('a'))

# # cari a href dalam link tersebut
# all_links = soup.find_all('a')
# for link in all_links:
#     print(link.get("href"))

# # cari table dalam link tersebut
# all_tables = soup.find_all('table')
# print(all_tables)

# # Extract the information to a dataframe
# right_table = soup.find_all(
#     'table', {"class": 'wikitable sortable plainrowheaders'})
# print(right_table)

# another extraction
right_table = soup.find('table', class_='wikitable sortable plainrowheaders')
# print(right_table)

#Generate lists
A = []
B = []
C = []
D = []
E = []
F = []
G = []
for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states = row.findAll('th')  # To store second column data
    if len(cells) == 6:  # Only extract table body not heading
        A.append(cells[0].find(text=True))
        B.append(states[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))


#import pandas to convert list to data frame
df = pd.DataFrame(A, columns=['Number'])
df['State/UT'] = B
df['Admin_Capital'] = C
df['Legislative_Capital'] = D
df['Judiciary_Capital'] = E
df['Year_Capital'] = F
df['Former_Capital'] = G

# save to csv
df.to_csv('out.csv', index=False)

print("\n")
print(df)
