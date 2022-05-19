from pprint import pprint
import requests
import time


class VkUser:
    url = 'https://api.vk.com/method'

    def __init__(self, token, version='5.131'):
        self.params = {
            'access_token': token,
            'v': version
        }

    def user_info(self, user_id ):
        info_params = {
            'user_ids': user_id,
            'fields': 'sex, universities, photo_max_orig'
        }
        res = requests.get(f'{self.url}/users.get', params={**self.params,**info_params}).json()
        return res

    def user_search(self, q, sex, count=50, sort=0, ):
        search_params = {
            'q': q,
            'fields': ' photo_id, verified, sex, bdate, city, country, home_town, has_photo, photo_50,'
                      ' photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig,'
                      ' online, lists, domain, has_mobile, contacts, site, education, universities, schools,'
                      ' status, last_seen, followers_count, common_count, occupation, nickname, relatives,'
                      ' relation, personal, connections, exports, wall_comments, activities, interests, music,'
                      ' movies, tv, books, games, about, quotes, can_post, can_see_all_posts, can_see_audio,'
                      ' can_write_private_message, can_send_friend_request, is_favorite, is_hidden_from_feed,'
                      ' timezone, screen_name, maiden_name, crop_photo, is_friend, friend_status, career,'
                      ' military, blacklisted, blacklisted_by_me',
            'sex': sex
        }
        res = requests.get(f'{self.url}/users.search', params={**self.params, **search_params}).json()
        return res

    def search_group(self, q, sorting=0):
        sg_params = {
            'q': q,
            'sort': sorting,
            'count': 30
        }
        res = requests.get(f'{self.url}/groups.search', params={**self.params, **sg_params})
        return res.json()



if __name__ == '__main__':
