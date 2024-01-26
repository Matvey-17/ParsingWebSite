from bs4 import BeautifulSoup
import requests

from info_site import header, data, url
from DB import Content

attr = {}

session = requests.Session()
response = session.post(url, headers=header, data=data)
profile_page = session.get(header['Origin'] + '/profile/edit/')

soup = BeautifulSoup(profile_page.text, 'html.parser')
info = soup.find_all('input')
content = soup.find_all('span', class_='name')

courses = ', '.join(set([line.text.strip() for line in content]))

for line in info:
    try:
        if line['name'] in ['first_name', 'last_name', 'middle_name', 'phone', 'email', 'vk']:
            attr[line['name']] = line['value']
    except KeyError:
        continue


def main():
    Content.table_create()
    Content(
        first_name=attr['first_name'],
        last_name=attr['last_name'],
        middle_name=attr['middle_name'],
        phone=attr['phone'],
        email=attr['email'],
        vk=attr['vk'],
        content=courses
    ).save()


if __name__ == '__main__':
    main()
