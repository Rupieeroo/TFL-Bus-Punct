import requests

request = requests.get('https://api.tfl.gov.uk/line/24/route/sequence/outbound')
route_json = request.json()
print(route_json['lineName'])
