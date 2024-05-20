from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_alive_server():
    response = client.get("/info")
    assert response.status_code == 200


def test_get_currency_with_date():
    response = client.get('/info/currency?currency=USD&date=24/05/2018').json()
    assert response['service'] == 'currency'
    assert response['data']['USD'] == 61.5945

    response = client.get('/info/currency?currency=UZS&date=24/05/2011').json()
    assert response['service'] == 'currency'
    assert response['data']['UZS'] == 16.6764
