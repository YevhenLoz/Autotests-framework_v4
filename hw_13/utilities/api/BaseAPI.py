from hw_13.configurations.config_file import BASE_URL, token
import requests


class BaseAPI:
    def __init__(self):
        self.__base_url = BASE_URL
        self.header = {'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)}
        self.__request = requests

    def get(self, url, headers=None):
        if headers is None:
            headers = self.header
        response = self.__request.get(f'{self.__base_url}{url}', headers=headers)
        return response

    def post(self, url, headers=None, body=None):
        if headers is None:
            headers = self.header
        response = self.__request.post(f'{self.__base_url}{url}', headers=headers, data=body)
        return response

    def delete(self, url, headers=None):
        if headers is None:
            headers = self.header
        response = self.__request.delete(f'{self.__base_url}{url}', headers=headers)
        return response


