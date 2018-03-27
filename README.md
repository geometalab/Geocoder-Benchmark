# Geocoder-Benchmark
Benchmarking some known Geocoder APIs using Python.

## Services

* Google
* Bing
* Nominatim
* OSMNames
* Mapcat
* Opencage

## Results

Geocoding with 1000 Addresses
Query:  `Street Streetnumber, Postal Code Zurich Switzerland`

#### Google

* Found:
    * Accuracy < 20m: 783
    * Accuracy < 100m: 156
    * Accuracy > 100m: 56
* Not found: 5

#### Bing

* Found:
    * Accuracy < 20m: 784
    * Accuracy < 100m: 125
    * Accuracy > 100m: 91
* Not found: 0

#### Nominatim

* Found:
    * Accuracy < 20m: 699
    * Accuracy < 100m: 76
    * Accuracy > 100m: 224
* Not found: 1

#### OSMNames

* Found:
    * Accuracy < 20m: 11
    * Accuracy < 100m: 205
    * Accuracy > 100m: 784
* Not found: 0

OSMNames is not suitable for geocoding because it does not return precise coordinates

#### Mapcat

* Found:
    * Accuracy < 20m: 288
    * Accuracy < 100m: 30
    * Accuracy > 100m: 257
* Not found: 425

Mapcat was sometimes really accurate with a difference of 0.2 meters but it couldn't find 425 addresses

#### Opencage

* Found:
    * Accuracy < 20m: 688
    * Accuracy < 100m: 82
    * Accuracy > 100m: 230
* Not found: 0
