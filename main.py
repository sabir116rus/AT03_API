import requests

def get_random_cat_image():
    url = 'https://api.thecatapi.com/v1/images/search'
    response = requests.get(url)
    if response.status_code == 200:
        # Возвращаем первый элемент из списка ответа, содержащий id, url, width и height
        return response.json()[0]
    else:
        return None
