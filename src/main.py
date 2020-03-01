import requests
import pprint

request = requests.get('https://api.tfl.gov.uk/StopPoint/490014138S/Arrivals')
route_json = request.json()

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

# pprint.pprint(route_json)
