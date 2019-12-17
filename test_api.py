import pytest
from api import BkkFutar


@pytest.fixture
def api():
    return BkkFutar()


@pytest.fixture()
def not_existing_api():
    return BkkFutar(host="https://fakehost.fakedomain.hu")


def test_none_response_when_connection_error(not_existing_api: BkkFutar):
    response = not_existing_api.search(None)
    assert response is None


def test_bicycle_rental(api: BkkFutar):
    response = api.bicycle_rental()
    assert response['status'] == 'OK'
    assert response['code'] == 200
    assert len(response['data']['list']) > 0


def test_alert_search_with_query(api: BkkFutar):
    response = api.alert_search("6")
    assert response['status'] == 'OK'
    assert response['code'] == 200
    assert len(response['data']['entry']['alertIds']) > 0


def test_alert_search_missing_empty_query(api: BkkFutar):
    response = api.alert_search("6")
    assert response['status'] == 'OK'
    assert response['code'] == 200
    assert len(response['data']['entry']['alertIds']) > 0


def test_search(api: BkkFutar):
    response = api.search("22")
    assert response['data']['entry'] is not None


def test_search_not_found(api: BkkFutar):
    response = api.search("adlkjfh")
    assert response['data']['entry'] is not None
