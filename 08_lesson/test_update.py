import requests

key = "tSSlM1Dt26-XSpdhOBdQOwWenXXorQaUeUanW9Nv4cXx-QNVCS0TCI2uS9Sr2kQl"

base_url = "https://ru.yougile.com/api-v2"
main_heders = {
            'Authorization': f'Bearer {key}',
            'Content-Type': 'application/json'
        }


def test_update():
    body = {"title": "Добрые улуги"}
    responses = requests.post(f"{base_url}/projects", headers=main_heders, json=body)
    assert responses.status_code == 201
    responses_body = responses.json()
    id = responses_body["id"]
    #запрос на редактирование
    body_new = {"title": "Ромашка"}
    responses = requests.put(f"{base_url}/projects/{id}",
         headers=main_heders, json=body_new)
    assert responses.status_code == 200
    #запрашиваем по id
    responses = requests.get(f"{base_url}/projects/{id}",
         headers=main_heders)
    assert responses.status_code == 200
    responses_body = responses.json()
    title = responses_body["title"]
    assert title == body_new["title"]


def test_update_negativ():
    body = {"title": "Добрые улуги"}
    responses = requests.post(f"{base_url}/projects",
         headers=main_heders, json=body)
    assert responses.status_code == 201
    responses_body = responses.json()
    id = responses_body["id"]
    #запрос на редактирование
    body_new = {"title": ""}
    responses = requests.put(f"{base_url}/projects/{id}",
         headers=main_heders, json=body_new)
    assert responses.status_code == 400
