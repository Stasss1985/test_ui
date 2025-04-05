import requests


# from urllib.parse import unquote
# Чтобы в консоли отображался текст без кодирования URL (т.е. в читаемом формате),
# вы можете использовать функцию urllib.parse.unquote. Эта функция декодирует URL,
# заменяя закодированные символы на их оригинальные значения.
# print(unquote(r.url)) # Декодируем URL

# Выполняем запрос
def test_get_pet_by_status():
    r = requests.get('https://petstore.swagger.io/v2/pet/findByStatus',
                     params={'status': 'available'})
    json_response = r.json()
    print(json_response[2])
    assert r.status_code == 200
    assert len(json_response) > 1


def test_post_pet():
    body = {
        "id": 5654,
        "category": {
            "id": 2,
            "name": "dogs"
        },
        "name": "kolobok",
        "photoUrls": [
            "http://dkdk.img"
        ],
        "tags": [
            {
                "id": 32,
                "name": "string"
            }
        ],
        "status": "available"
    }
    r = requests.post('https://petstore.swagger.io/v2/pet',
                      json=body,
                      auth=('login', 'password'))  # авторизация по логину и паролю

    assert r.status_code == 200


def test_post_pet_autoriz():
    body = {
        "id": 5654,
        "category": {
            "id": 2,
            "name": "dogs"
        },
        "name": "kolobok",
        "photoUrls": [
            "http://dkdk.img"
        ],
        "tags": [
            {
                "id": 32,
                "name": "string"
            }
        ],
        "status": "available"
    }
    headers = {"Autorization": "special-key"}  # для меня "Autorization": "Bearer accesstoken"
    r = requests.post('https://petstore.swagger.io/v2/pet',
                      json=body,
                      headers=headers)  # авторизация по accesstoken или "special-key"

    assert r.status_code == 200


def test_post_autoriz():
    body = {
        "id": 5654,
        
        }
    headers = {"Autorization": "Bearer eyJ0eXAiOiJKV1QiLCJ}
    r = requests.post('https://e.ru/oauth/token',
                      json=body,
                      headers=headers)  # авторизация по accesstoken или "special-key"

    assert r.status_code == 200


