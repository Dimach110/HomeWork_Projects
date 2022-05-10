from pprint import pprint
import requests
from yadisk import YaDisk

if __name__ == '__main__':
    path_to_file = 'test_file.txt' # можно указать любой файл
    token = '...'
    uploader = YaDisk(token)
    result = uploader.upload_file(path_to_file, path_to_file)