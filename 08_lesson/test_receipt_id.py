import requests

key = "tSSlM1Dt26-XSpdhOBdQOwWenXXorQaUeUanW9Nv4cXx-QNVCS0TCI2uS9Sr2kQl"

base_url = "https://ru.yougile.com/api-v2"
main_heders = {
            'Authorization': f'Bearer {key}',
            'Content-Type': 'application/json'
        }


def test_receipt_id():
    body = {"title": "Лютик"}
    responses = requests.post(f"{base_url}/projects",
           headers=main_heders, json=body)
    assert responses.status_code == 201
    responses_body = responses.json()
    id = responses_body["id"]
    #запрашиваем по id
    responses = requests.get(f"{base_url}/projects/{id}",
           headers=main_heders)
    assert responses.status_code == 400
    responses_body = responses.json()
    title = responses_body["title"]
    assert title == body["title"]


def test_receipt_id_negativ():
    body = {"title": "Одуванчик"}
    responses = requests.post(f"{base_url}/projects",
          headers=main_heders, json=body)
    assert responses.status_code == 201
    responses_body = responses.json()
    id = responses_body["id"]
    # запрашиваем по id
    responses = requests.get(f"{base_url}/projects/9999999",
           headers=main_heders)
    assert responses.status_code == 404
    responses_body = responses.json()
    title = responses_body["title"]
    assert title == body["title"]
