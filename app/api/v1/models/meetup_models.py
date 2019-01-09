import json

meetups = []

class Meetups:
    """The class for the meetups"""
    def __init__(self, meetupid, createdOn, createdBy, location, topic, happeningOn, tags):
        """The meetup constructor"""
        self.meetupid = len(meetups)+1
        self.createdOn = createdOn
        self.createdBy = createdBy
        self.location = location
        self.topic = topic
        self.tags = tags
        self.happeningOn = happeningOn

    def create_meetup(self):
        the_meetup = {
            "topic":self.topic,
            "location":self.location,
            "happeningOn":self.happeningOn,
            "tags":self.tags
        }

        self.meetups.append(the_meetup)
        return meetup
        
