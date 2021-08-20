## BKK Futar API Python client

BKK Futar is a service of Budapest Transportation company to provide realtime information about Budapest public transportation including live vehicle tracking, stop times, schedules, route information etc. 
Webiste: (http://futar.bkk.hu)

The goal of this simple project to wrap available methods into a class collected from [BKK FUTÁR Utazásszervező API](https://bkkfutar.docs.apiary.io) documentation.

Source code: [Github](https://github.com/gabor-simon/bkk-futar-python-client)

Before using the package, you need to install it trough pip:
> pip install bkkfutar

Sample usage:
````python
import futar

api = futar.BkkFutar()
response = api.arrivals_and_departures_for_stop("BKK_F01004")
stop_times = response['data']['entry']['stopTimes']
print(stop_times)
````
