import requests as rq
from bs4 import BeautifulSoup as bs
import csv

def create_csv_data():
    r = rq.get('http://messier.obspm.fr/CONindex2_f.html')

    soup = bs(r.content, 'html.parser')

    data = []

    for x in soup.ul.find_all('li', recursive=False):
        row = dict()
        row['galaxy_name'] = x.i.a.get_text().strip()
        row['galaxy_link'] = 'http://messier.obspm.fr/' + x.i.a['href']

        for y in x.ul.find_all('li'):
            messier = dict()
            try:
                surname = ' '.join(y.b.get_text().split())
            except AttributeError:
                surname = ''

            messier['messier_name'] = y.a.get_text().strip()
            messier['messier_link'] = 'http://messier.obspm.fr/' + y.a['href']
            messier['messier_surname'] = surname.replace(',', '')
            messier['messier_form'] = ' '.join(list(filter(None, [x.strip() for x in y(recursive=False, text=True)])))

            r_messier = rq.get(messier['messier_link'])

            soup_messier = bs(r_messier.content, 'html.parser')

            messier.update(row)

            data.append(messier)

    with open("data.csv","w",newline="") as file_writer:
        fields=['messier_name','messier_link','messier_surname','messier_form','galaxy_name','galaxy_link']
        writer=csv.DictWriter(file_writer,fieldnames=fields)
        writer.writeheader()
        for x in data:
            writer.writerow(x)