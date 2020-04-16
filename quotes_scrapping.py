import requests, csv
from bs4 import BeautifulSoup

responce = requests.get('http://quotes.toscrape.com/')
html_data = BeautifulSoup(responce.text, features='html.parser')
quotes = html_data.find_all(class_='quote')
quote_list = []
for quote in quotes:
    quote_1 = [quote.find(class_='text').get_text(),
               quote.find(class_='author').get_text(),
               quote.find(class_='keywords')['content']]
    quote_list.append(quote_1)


with open ('quotes.csv', 'w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Text', 'Author', 'Keywords'])
    for row in quote_list:
        csv_writer.writerow(row)