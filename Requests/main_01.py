from pprint import pprint
import requests
from yadisk import YaDisk

YANDEX_TOKEN = '...'

if __name__ == '__main__':
    yadisk = YaDisk(YANDEX_TOKEN)
    # for file in yadisk.get_files_list()['items']:
    #     print(file['name'], end=" = ")
    #     print(f"{file['size']} байт")
    # # pprint(yadisk.get_files_list())
    yadisk.upload_file('/new/My_test_file.txt', 'test_file.txt')