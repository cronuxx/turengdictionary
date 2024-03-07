from bs4 import BeautifulSoup as bs
import cloudscraper

def en_tr():
    tables = soup.find_all('table', {'class': 'table table-hover table-striped searchResultsTable'})
    c2 = tables[0].find_all('tr')[0].find_all('th', {'class': 'c2'})
    c2_text = c2[0].text
    if c2_text == 'İngilizce':

        table_tr = tables[0].find_all('tr')
        x = len(table_tr)

        for i in range(3, x):
            category = table_tr[i].find_all('td',{'class':'hidden-xs'})

            a = table_tr[i].find_all('a')

            if len(a) == 0 and len(category) == 0:
                pass
            else:

                print(f'{category[1].text} - {a[1].text}')
    else:
        table_tr = tables[1].find_all('tr')
        x = len(table_tr)
        for i in range(3, x):
            category = table_tr[i].find_all('td', {'class': 'hidden-xs'})
            a = table_tr[i].find_all('a')

            if len(a) == 0 and len(category) == 0:
                pass
            else:
                print(f'{category[1].text} - {a[1].text}')

def tr_en():
    tables = soup.find_all('table', {'class': 'table table-hover table-striped searchResultsTable'})
    c2 = tables[0].find_all('tr')[0].find_all('th', {'class': 'c2'})
    c2_text = c2[0].text
    if c2_text == 'Türkçe':

        table_tr = tables[0].find_all('tr')
        x = len(table_tr)
        for i in range(3, x):
            category = table_tr[i].find_all('td', {'class': 'hidden-xs'})

            a = table_tr[i].find_all('a')

            if len(a) == 0 and len(category) == 0:
                pass
            else:
                print(f'{category[1].text} - {a[1].text}')
    else:
        table_tr = tables[1].find_all('tr')
        x = len(table_tr)
        for i in range(3, x):
            category = table_tr[i].find_all('td', {'class': 'hidden-xs'})
            a = table_tr[i].find_all('a')

            if len(a) == 0 and len(category) == 0:
                pass
            else:
                print(f'{category[1].text} - {a[1].text}')
while True: 
    word = input('Word: ')

    scraper = cloudscraper.create_scraper(delay=10, browser='chrome') 
    url = f"https://tureng.com/tr/turkce-ingilizce/{word}"

    info = scraper.get(url).text

    soup = bs(info, "html.parser")


    if soup.find("h1").text == "Sanırız yanlış oldu, doğrusu şunlar olabilir mi?":
            print(f'There is no such thing as a {word}.')
            
    else:
            language = input('en_TR - tr_EN: ')
            if language == 'en_TR':
                en_tr()
            else:
                tr_en()
