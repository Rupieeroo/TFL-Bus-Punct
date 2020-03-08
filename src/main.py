#!/usr/bin/env python3

import requests
import csv
from dataclasses import dataclass, asdict
from sys import stdout

request = requests.get('https://api.tfl.gov.uk/StopPoint/490014138S/Arrivals')
route_json = request.json()


@dataclass
class Stop:
    route_no = int

    def stop_points(self):
        stop_point = requests.get(f'https://api.tfl.gov.uk/Line/{self.route_no}/StopPoints')
        stoppoint_codes = stop_point.json()

        for s in stoppoint_codes:
            yield s['stationNaptan']
            yield s['commonName']
            yield s['additionalProperties'][1]['value']


def route_finder():
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


if __name__ == "__main__":
    data_table = csv.DictWriter(
        stdout, ['Station_naptan', 'Name', 'Direction']
    )
    data_table.writeheader()
    for row in Stop().stop_points(24):
        data_table.writerow(asdict(row))
