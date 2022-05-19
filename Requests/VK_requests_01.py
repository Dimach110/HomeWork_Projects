from pprint import pprint
import requests
import time

url = 'https://api.vk.com/method'
token = 'bc2b91e2ce1e94e69513f5cdaec19f9fcced8505e612541c8908882e4e68894eba6ee38778ff315b3f9b6'
# params = {
#     'user_ids': '2606515',
#     'access_token': f'{token}',
#     'v': '5.131',
#     'fields': 'sex, universities, photo_max_orig, personal'
# }

params = {
    'q': 'phyton',
    'access_token': f'{token}',
    'v': '5.131',
    'sort': '0',
    'count': 20
}

# res = requests.get(f'{url}/users.get', params=params).json()
res = requests.get(f'{url}/groups.search', params=params).json()
pprint(res)


# if __name__ == '__main__':