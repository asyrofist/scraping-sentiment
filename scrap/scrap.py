# library
import bs4 as bs
import lxml
from urllib import request
import urllib

# preprocessing
# source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface').read()
link_url = input("masukkan url: ")
source = urllib.request.urlopen(link_url).read()
soup = bs.BeautifulSoup(source, 'lxml')

# link url yang dimuat
print(soup)

# # title url
# print(soup.title)

# # title name
# print(soup.title.name)

# # title string
# print(soup.title.string)

# # body pargraph url
# print(soup.p)

# # cari semua paragraph
# print(soup.find_all('p'))

# # cari semua paraph dalam bentuk text
# for paragraph in soup.find_all('p'):
#     print(paragraph.text)

# tampilkan dalam format url tanpa karakter
# print(soup.get_text())

# # cari komponen sesuai dengan format a
# for url in soup.find_all('a'):
#     print(url.text)

# # cari component yang terdapat karakter href.
# for url in soup.find_all('a'):
#     print(url.get('href'))

# # navigation
# nav = soup.nav

# # tampilkan navigasi
# print(nav)

# # cari karakter a href
# for url in nav.find_all('a'):
#     print(url.get('href'))

# # cari karakter p
# body = soup.body
# for paragraph in body.find_all('p'):
#     print(paragraph.text)

# # cari karakter div
# for div in soup.find_all('div'):
#     print(div.text)

# # cari div dibagian body
# for div in soup.find_all('div', class_='body'):
#     print(div.text)

# # buat tabel
# table = soup.table
# print(table)

# # atau bisa dengan begini mencari table
# table = soup.find('table')
# print(table)

# #cari tabel dengan karakter tr
# table_rows = table.find_all('tr')
# print(table_rows)

# # buat tabel sesuai row
# for tr in table_rows:
#     td = tr.find_all('td')
#     row = [i.text for i in td]
#     print(row)
