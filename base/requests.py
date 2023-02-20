import requests


def get_data_from_gutendex():
    result = requests.get('https://gutendex.com/books/?page=1')
    return result.json()['results']
