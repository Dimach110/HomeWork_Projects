from pprint import pprint

import requests

class YaDisk:
    host = 'https://cloud-api.yandex.net'

    def __init__(self, token):
        self.token = token

    def get_header(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_files_list(self):
        url = f'{self.host}/v1/disk/resources/files/'
        headers = self.get_header()
        response = requests.get(url, headers=headers)
        return response.json()

    def _get_upload_link(self, path):   # Получаем ссылку для загрузки файла
        url = f'{self.host}/v1/disk/resources/upload'
        headers = self.get_header()
        params = {'path': path, 'overwrite': True}
        response = requests.get(url, headers=headers, params=params)
        pprint(response.json())
        return response.json().get('href')

    def upload_file(self, path, file_name):
        upload_link = self._get_upload_link(path)
        headers = self.get_header()
        response = requests.put(upload_link, data=open(file_name, 'rb'), headers=headers)
        response.raise_for_status()    # Запрашиваем статус
        if response.status_code == 201:
            print("The file upload was successful")
