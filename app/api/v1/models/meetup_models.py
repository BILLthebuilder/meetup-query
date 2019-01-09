from datetime import datetime, timedelta

MEETUPS = []

class MeetUpModel(object):
    """ Mapping meetup and data relations """

    def __init__(self):
        self.meetups = MEETUPS

    def create_meetup(self, topic, location, images, happeningOn, tags):
        """ A constructor method for the meetups """

        createdOn = datetime.now()
        meetup = {
            "id": len(self.meetups) + 1,
            "topic": topic,
            "location": location,
            "createdOn": createdOn,
            "happeningOn": happeningOn,
            "images": images,
            "tags": tags,
        }

        self.meetups.append(meetup)
        return meetup

    def view_meetups(self):
        if len(self.meetups) == 0:
            return ({
                "message": "There are no meetups"
            })
        return self.meetups

    def view_one_meetup(self, id):
        """ A method to view one meetup """
        return [meetup for meetup in MEETUPS if meetup["id"] == id]
        

# import json

# meetups = []

# class Meetups:
#     """The class for the meetups"""
#     def __init__(self, meetupid, createdOn, createdBy, location, topic, happeningOn, tags):
#         """The meetup constructor"""
#         self.meetupid = len(meetups)+1
#         self.createdOn = createdOn
#         self.createdBy = createdBy
#         self.location = location
#         self.topic = topic
#         self.tags = tags
#         self.happeningOn = happeningOn

#     def create_meetup(self):
#         the_meetup = {
#             "topic":self.topic,
#             "location":self.location,
#             "happeningOn":self.happeningOn,
#             "tags":self.tags
#         }

#         self.meetups.append(the_meetup)
#         return meetup
