import requests
from pprint import pprint
URL = 'https://superheroapi.com/api/2619421814940190'

def response_hero(name_hero):
    response = requests.get(f'{URL}/search/{name_hero}')
    return response.json()

class Hero():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __lt__(self, other):
        if int(self.response_hero_intelligence()['intelligence']) > int(other.response_hero_intelligence()['intelligence']):
            return f'{self.name} more intelligent {other.name}'
        else:
            return f'{other.name} more intelligent {self.name}'

    def response_hero_intelligence(self):
        response = requests.get(f'{URL}/{self.id}/powerstats')
        return response.json()

if __name__ == '__main__':
    # Определил ID каждого героя
    # pprint(response_hero('Hulk')) # id 332 (int=88)
    # pprint(response_hero('Captain America')) # id 149 (int=69)
    # pprint(response_hero('Thanos')) # id 655 (int=100)

    Hulk = Hero('332', 'Hulk')
    CA = Hero('149', 'Captain America')
    Thanos = Hero('655', 'Thanos')
    # Проводим сравнение между героями
    print(CA.__lt__(Hulk))
    print(Thanos.__lt__(Hulk))
    print(Thanos.__lt__(CA))

