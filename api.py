import requests
import logging


class BkkFutar:
    HOST = "https://futar.bkk.hu"
    KEY = "PyFutar"
    API_PATH = "api/query/v1/ws/otp/api/where"

    def __init__(self, host=HOST, path=API_PATH, key=KEY, include_references=True):
        self.host = host
        self.uri = f"{host}/{path}"
        self.params = {"includeReferences": "true" if include_references in (True, None) else "false",
                       "key": key,
                       "version": "3"}
        self.headers = {"Content-Type": "application/json"}
        self._logger = logging.getLogger("")

    def _call_endpoint(self, endpoint, headers, params):
        try:
            response = requests.get(endpoint, headers=headers, params=params)
        except requests.exceptions.RequestException as err:
            self._logger.error(err)
            return None
        return response.json()

    def bicycle_rental(self, include_references=True):
        endpoint = f"{self.uri}/bicycle-rental.json"
        params = self.params
        params.update({"includeReferences": "true" if include_references in (True, None) else "false"})
        return self._call_endpoint(endpoint, self.headers, params)

    def alert_search(self, query, start=None, end=None, include_references=True):
        endpoint = f"{self.uri}/alert-search.json"
        params = self.params
        params.update({"query": query,
                       "start": start,
                       "end": end,
                       "includeReferences": "true" if include_references in (True, None) else "false"})
        return self._call_endpoint(endpoint, self.headers, params)

    def search(self, query, include_references=True):
        endpoint = f"{self.uri}/search.json"
        params = self.params
        params.update({"query": query,
                       "includeReferences": "true" if include_references in (True, None) else "false"})
        return self._call_endpoint(endpoint, self.headers, params)

    def stops_for_location(self, lon, lat, lon_span=None, lat_span=None, radius=100, query="", include_references=True):
        endpoint = f"{self.uri}/stops-for-location.json"
        params = self.params
        params.update({"lon": lon,
                       "lat": lat,
                       "lonSpan": lon_span,
                       "latSpan": lat_span,
                       "radius": radius,
                       "query": query,
                       "includeReferences": "true" if include_references in (True, None) else "false"
                       })
        return self._call_endpoint(endpoint, self.headers, params)

    def arrivals_and_departures_for_stop(self, stopid, only_departures=False, minutes_before=0, minutes_after=30,
                                         limit=60, include_references=True):
        endpoint = f"{self.uri}/arrivals-and-departures-for-stop.json"
        params = self.params
        params.update({"stopId": stopid,
                       "minutesBefore": minutes_before,
                       "minutesAfter": minutes_after,
                       "limit": limit,
                       "includeReferences": "true" if include_references in (True, None) else "false",
                       "onlyDepartures": "true" if only_departures in (True, None) else "false"})
        return self._call_endpoint(endpoint, self.headers, params)

    def arrivals_and_departures_for_location(self, lon, lat, lon_span=None, lat_span=None, only_departures=False,
                                             limit=60, minutes_before=2, minutes_after=30,
                                             group_limit=4, client_lon=None, client_lat=None):
        endpoint = f"{self.uri}/arrivals-and-departures-for-location.json"
        params = self.params
        params.update({"lon": lon,
                       "lat": lat,
                       "lonSpan": lon_span,
                       "latSpan": lat_span,
                       "onlyDepartures": "true" if only_departures in (True, None) else "false",
                       "limit": limit,
                       "minutesBefore": minutes_before,
                       "minutesAfter": minutes_after,
                       "groupLimit": group_limit,
                       "clientLon": client_lon,
                       "clientLat": client_lat
                       })
        return self._call_endpoint(endpoint, self.headers, params)

    def schedule_for_stop(self, stopid, date, only_departures=False):
        endpoint = f"{self.uri}/schedule-for-stop.json"
        params = self.params
        params.update({"stopId": stopid,
                       "onlyDepartures": "true" if only_departures in (True, None) else "false",
                       "date": date
                       })
        return self._call_endpoint(endpoint, self.headers, params)

    def route_details(self, routeid, related=False, include_references=True):
        endpoint = f"{self.uri}/route-details.json"
        params = self.params
        params.update({"routeId": routeid,
                       "includeReferences": "true" if include_references in (True, None) else "false",
                       "related": "true" if related in (True, None) else "false"
                       })
        return self._call_endpoint(endpoint, self.headers, params)

    def trip_details(self, tripid, vehicle_id, date, include_references=True):
        endpoint = f"{self.uri}/trip-details.json"
        params = self.params
        params.update({"tripId": tripid,
                       "vehicleId": vehicle_id,
                       "includeReferences": "true" if include_references in (True, None) else "false",
                       "date": date
                       })
        return self._call_endpoint(endpoint, self.headers, params)

    def vehicles_for_location(self, lon, lat, radius=100, query="", lon_span=None,
                              lat_span=None, include_references=True):
        endpoint = f"{self.uri}/vehicles-for-location.json"
        params = self.params
        params.update({"lon": lon,
                       "lat": lat,
                       "radius": radius,
                       "query": query,
                       "lonSpan": lon_span,
                       "latSpan": lat_span,
                       "includeReferences": "true" if include_references in (True, None) else "false"
                       })
        return self._call_endpoint(endpoint, self.headers, params)

    def vehicles_for_route(self, route_id, related=False, include_references=True):
        endpoint = f"{self.uri}/vehicles-for-route.json"
        params = self.params
        params.update({"routeId": route_id,
                       "related": "true" if related in (True, None) else "false",
                       "includeReferences": "true" if include_references in (True, None) else "false"
                       })
        return self._call_endpoint(endpoint, self.headers, params)

    def vehicles_for_stop(self, stopid, include_references=True):
        endpoint = f"{self.uri}/vehicles-for-stop.json"
        params = self.params
        params.update({"stopId": stopid,
                       "includeReferences": "true" if include_references in (True, None) else "false"
                       })
        return self._call_endpoint(endpoint, self.headers, params)


def main():
    api = BkkFutar()
    print(api.vehicles_for_stop("BKK_F04683"))
    pass


if __name__ == '__main__':
    main()
