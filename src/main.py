import requests
import pprint

request = requests.get('https://api.tfl.gov.uk/StopPoint/490014138S/Arrivals')
stop_points = requests.get('https://api.tfl.gov.uk/Line/127/StopPoints')
route_json = request.json()
stoppoint_codes = stop_points.json()

for s in stoppoint_codes:
    print(s['stationNaptan'])
    print(s['commonName'])

for p in route_json:
    if p['expectedArrival'] <= p['timeToLive']:
        print(f"The {p['lineName']}")
        print(f"arriving at {p['stationName']}")
        print(f"towards {p['towards']}")
        print('is on time')
    else:
        print(f"The {p['lineName']}")
        print(f"arriving at {p['stationName']}")
        print(f"towards {p['towards']}")
        print('is late')

# pprint.pprint(stoppoint_codes)
