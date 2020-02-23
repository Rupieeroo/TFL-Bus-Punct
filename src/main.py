import requests
import pprint

request = requests.get('https://api.tfl.gov.uk/line/24/route/sequence/outbound')
route_json = request.json()

for p in route_json['stations']:
    for l in p['lines']:
        if p['lines'][0]['id'] == '24':
            print(p['name'])

# pprint.pprint(route_json['stations'])