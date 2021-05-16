
class Sensor:

    identification = 0

    def __init__(self, coordinates):
        self._id = Sensor.identification
        Sensor.identification = Sensor.identification + 1

        self._coordinates = coordinates
        self._vacancy = 0

    def check_vacancy(self):
        return self._vacancy

    def set_vacancy(self):
        self._vacancy = 1

    def set_free(self):
        self._vacancy = 0

    def get_id(self):
        return self._id

    def set_id(self, identification):
        self._id = identification

    def get_coordinates(self):
        return self._coordinates

    def set_coordinates(self, coordinates):
        self._coordinates = coordinates


if __name__ == '__main__':

    sensor = Sensor((4,5))

    print(sensor.get_coordinates())
    print(sensor.check_vacancy())

    sensor.set_vacancy()
    print(sensor.check_vacancy())

    sensor.set_free()
    print(sensor.check_vacancy())
