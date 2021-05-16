from Sensor_Data_API import Sensor
from flask import Flask


class Sensor_Manager:

    def initiate_api(self):

        api = Flask(__name__)

        @api.route('/')
        def return_spots():
            return self.spots_api()

        api.run()

    def __init__(self, sensor_list):

        self._sensor_list = []
        for sensor in sensor_list:
            if isinstance(sensor, Sensor):
                self._sensor_list.append(sensor)

        self._available_spots = []

        self.initiate_api()

    def check_available_spots(self):

        self._available_spots = []
        for sensor in self._sensor_list:
            if sensor.check_vacancy():
                self._available_spots.append(sensor.get_coordinates())

    def spots_api(self):

        self.check_available_spots()
        json_spots = {"Spots": self._available_spots}
        return json_spots


if __name__ == '__main__':

    sensor1 = Sensor((4, 5))
    sensor1.set_vacancy()

    sensor2 = Sensor((10, 15))
    sensor2.set_vacancy()

    sensor3 = Sensor((20, 40))
    sensor3.set_vacancy()

    sensor_list = [sensor1, sensor2, sensor3]

    manage_sensor = Sensor_Manager(sensor_list)

    while True:
        continue

