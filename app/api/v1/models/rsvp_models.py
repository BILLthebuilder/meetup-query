import datetime

RESERVATIONS = []


class RsvpModel():
    """ Mapping reservations and data relations """

    def __init__(self):
        self.reservations = RESERVATIONS

    def save(self, topic, status):
        """ The reservations db """

        reserves = {
            "topic": topic,
            "createdOn": datetime.datetime.now(),
            "id": len(self.reservations) + 1,
            "status": status
        }

        self.reservations.append(reserves)
        return self.reservations
