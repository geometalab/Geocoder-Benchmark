import geocoder, csv, time, os, json
from math import sin, cos, sqrt, atan2, radians

SAMPLE = 'Vorlage in WGS84.csv'
INTERIM_RESULT_FILENAME = 'Zwischenergebnisse.csv'
RESULT_FILENAME = 'Ergebnisse für Mapcat.csv'

API_KEYS = json.load(open("config.json"))


def geocoding():
    with open(SAMPLE, 'r') as csv_input:
        reader = csv.reader(csv_input, delimiter=';')
        next(reader, None)
        rows = []
        easting = []
        northing = []
        error_counter = 0
        counter = 0
        for row in reader:
            new_row = row[2] + ' ' + row[3] + ', ' + row[0] + ' Zürich Switzerland'
            rows.append(new_row)
        start = time.time()
        for row in rows:
            # g = geocoder.google(row, key=API_KEYS['apis'][0]['googleapi_diego'])
            # g = geocoder.opencage(row, key=API_KEYS['apis'][0]['opencage'])
            # g = geocoder.bing(row, key=API_KEYS['apis'][0]['bing_diego'])
            # g = geocoder.osm(row)
            # g = geocoder.osmn(row)
            g = geocoder.mapcat(row, key=API_KEYS['apis'][0]['mapcat'])

            if g.latlng is not None:
                counter += 1
                print(counter)
                print(g.latlng)
                easting.append(g.latlng[0])
                northing.append(g.latlng[1])
            else:
                error_counter += 1
                easting.append('not found')
                northing.append('not found')
        print(error_counter, 'location(s) not found')
        end = time.time()
        print(round((end - start), 3))
        csv_append_easting(easting, northing)


def csv_append_easting(easting, northing):
    with open(SAMPLE, 'r') as csv_input:
        with open(INTERIM_RESULT_FILENAME, 'w') as csv_output:
            writer = csv.writer(csv_output, lineterminator='\n', delimiter=';')
            reader = csv.reader(csv_input, delimiter=';')

            all = []
            row = next(reader)
            row.append('E')
            row.append('N')
            all.append(row)

            for r, e, n in zip(reader, easting, northing):
                r.append(str(n))
                r.append(str(e))
                all.append(r)

            writer.writerows(all)


def calculate_distance():
    with open(INTERIM_RESULT_FILENAME, 'r') as csv_input:
        with open(RESULT_FILENAME, 'w') as csv_output:
            writer = csv.writer(csv_output, lineterminator='\n', delimiter=';')
            reader = csv.reader(csv_input, delimiter=';')
            all = []
            rows = next(reader, None)
            rows.append('Distance')
            all.append(rows)
            for r in reader:
                try:
                    # approximate radius of earth in km
                    R = 6373.0

                    lat1 = radians(float(r[4]))
                    lon1 = radians(float(r[5]))
                    lat2 = radians(float(r[6]))
                    lon2 = radians(float(r[7]))

                    dlon = lon2 - lon1
                    dlat = lat2 - lat1

                    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
                    c = 2 * atan2(sqrt(a), sqrt(1 - a))

                    distance = round(((R * c) * 1000), 2)
                    # print("Result:", distance, 'm')
                    r.append(distance)
                    all.append(r)
                except ValueError:
                    all.append(r)
                    continue
            writer.writerows(all)
    os.remove(INTERIM_RESULT_FILENAME)


if __name__ == "__main__":
    geocoding()
    calculate_distance()
