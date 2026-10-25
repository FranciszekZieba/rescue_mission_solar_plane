"""
ze wzgledu ze jest to tylko symmulacja postanowilem wykrywanie celu
zrealizowac poprzez zadanie programowi punkty docelowego, do którego
odleglosc będzie sprawdzana co chwile. jezeli odleglosc spadnie do
odpowiednio malej dron zatrzyma sie i zrzuci ladunek
"""

import math

class TargetDetector:
    def __init__(self, target_lat, target_lon, threshold=8.0):
        self.target_lat = target_lat
        self.target_lon = target_lon
        self.threshold = threshold

    def detection(self, curr_lat, curr_lon):

        d_lat = (curr_lat - self.target_lat) * 111000
        d_lon = (curr_lon - self.target_lon) * 111000 * math.cos(
            math.radians(self.target_lat)
        )
        distance = math.sqrt(d_lat ** 2 + d_lon ** 2)

        if distance <= self.threshold:
            print("cel wykryty")
            return True

        return False
