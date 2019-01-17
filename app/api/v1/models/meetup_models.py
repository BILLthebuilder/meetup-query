import datetime

MEETUPS = []


class MeetupData():
    """ Mapping meetup and data relations """

    def __init__(self):
        self.meetup_records = MEETUPS

    def save(self, title, description, date, location):
        data = {
            "createdOn": datetime.datetime.now(),
            "id": len(self.meetup_records)+1,
            "title": title,
            "description": description,
            "date": date,
            "location": location
        }

        self.meetup_records.append(data)
        return self.meetup_records

    def view_meetups(self):
        if len(self.meetup_records) == 0:
            return ({
                "message": "There are no meetup_records"
            })
        return self.meetup_records

    def view_one_meetup(self, id):
        """ A method to view one meetup """
        item = None
        for record in self.meetup_records:
            if record['id'] == id:
                item = record
        return item
