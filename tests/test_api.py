import pytest

from futar import BkkFutar


@pytest.fixture
def api():
    return BkkFutar()


@pytest.fixture()
def not_existing_api():
    return BkkFutar(host="https://fakehost.fakedomain.hu")


def test_none_response_when_connection_error(not_existing_api: BkkFutar):
    with pytest.raises(ConnectionError):
        not_existing_api.search(None)


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


def test_search(api: BkkFutar):
    response = api.search("22")
    assert len(response['data']['entry']['routeIds']) > 0


def test_stops_for_location(api: BkkFutar):
    response = api.stops_for_location(47.507477, 19.025309, query="Széll Kálmán")
    assert len(response['data']['list']) > 0


def test_arrivals_and_departures_for_stop(api: BkkFutar):
    response = api.arrivals_and_departures_for_stop("BKK_F01004")
    assert len(response['data']['entry']['stopTimes']) > 0


@pytest.mark.skip(reason="Skipped, because not sure this endpoint has been implemented")
def test_arrivals_and_departures_for_location(api: BkkFutar):
    response = api.arrivals_and_departures_for_location("47.477900", "19.045807",
                                                        client_lon="47.477900", client_lat="19.045807")
    assert response['data']['entry']['stopTimes'] > 0


def test_route_deteails(api: BkkFutar):
    response = api.route_details("BKK_3040")
    assert response['data']['entry']['id'] == "BKK_3040"


def test_trip_details_not_found(api: BkkFutar):
    response = api.trip_details("BKK_B132611", "BKK_4419")
    assert response['status'] == 'NOT_FOUND'


def test_vehicles_for_location(api: BkkFutar):
    response = api.vehicles_for_location(47.507466, 19.025225)
    assert len(response['data']['list']) > 0


def test_vehicles_for_route(api: BkkFutar):
    response = api.vehicles_for_route("BKK_0221")
    assert len(response['data']['list']) > 0


def test_vehicles_for_stop(api: BkkFutar):
    response = api.vehicles_for_stop("BKK_F01004")
    assert len(response['data']['list']) > 0
