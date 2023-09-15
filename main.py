from modules.book import Book
from modules.magazine import Magazine
from modules.cd import Cd
from modules.dvd import Dvd
from modules.catalog import Catalog
import json

with open('./files/data.json', mode='r+') as f:
    data_json = json.load(f)

list_book = []
list_magazine = []
list_dvd = []
list_cd = []

for item in data_json:
    if item['source'] == 'book':
        list_book.append(Book(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            isbn=item['issbn'],
            authors=item['authors'],
            dds_number=item['dds_number']
            ))
    elif item['source'] == 'magazine':
        list_magazine.append(Magazine(
            title=item['title'],
            upc=item['upc'],
            subject=item['subject'],
            volume=item['volume'],
            issue=item['issue'],
        ))
    elif item['source'] == 'cd':
        list_magazine.append(Cd(
            title=item['title'],
            upc=item['upc'],
            subject=item['subject'],
            artist=item['artist'],
        ))
    elif item['source'] == 'dvd':
        list_magazine.append(Dvd(
            title=item['title'],
            upc=item['upc'],
            subject=item['subject'],
            actors=item['actors'],
            director=item['directors'],
            genre=item['genre']
        ))

catalog_all = [list_book, list_magazine, list_dvd, list_cd]  
input_search = 'test'
result = Catalog(catalog_all).search(input_search)

print('====| results |====')
for index, result in enumerate(result):
    print(f'result ke-{index+1} | {result}')

# print(list_book)
# print(list_magazine)
# print(list_cd)
# print(list_dvd)