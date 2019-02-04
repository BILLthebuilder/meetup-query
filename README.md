# meetup-query

[![Build Status](https://travis-ci.org/BILLthebuilder/meetup-query.svg?branch=develop)](https://travis-ci.org/BILLthebuilder/meetup-query)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/23dc6c0874104fca8473fd8d59ea2067)](https://www.codacy.com/app/BILLthebuilder/meetup-query?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=BILLthebuilder/meetup-query&amp;utm_campaign=Badge_Grade)
[![codecov](https://codecov.io/gh/BILLthebuilder/meetup-query/branch/develop/graph/badge.svg)](https://codecov.io/gh/BILLthebuilder/meetup-query)
[![Maintainability](https://api.codeclimate.com/v1/badges/fbc43151aa7a1cb8a6a0/maintainability)](https://codeclimate.com/github/BILLthebuilder/meetup-query/maintainability)

## About

meetup-query is a web application that crowd-sources questions for a meetup. 'meetup-query' helps the meetup organizer prioritize questions to be answered. Other users can vote on asked questions and they bubble to the top or bottom of the log.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

* Python 3.6.7
  
* Postman
  
### Installing

A step by step series of examples that tell you how to get a development environment running

* Clone the project repository
  
`git clone https://github.com/BILLthebuilder/meetup-query.git`

* Change the directory
  
`cd meetup-query`

* Install the virtual environment
  
`virtualenv venv`

* Activate the virtual environment
  
`source/venv/bin/activate`

* Install the dependencies
  
`pip install -r requirements.txt`

* Run the application
    ```bash
      export FLASK_APP=run.py
      export FLASK_ENV=development
      export FLASK_DEBUG=1
      flask run
    ```

### The API Endpoints

| Request | Endpoint                              | Function                                          |
| ------- | ------------------------------------- | ------------------------------------------------- |
| POST    | `/api/v1/meetups`                     | Create a Meetup record                            |
| GET     | `/api/v1/meetups/<int:id>`            | Fetch a Specific Meetup record                    |
| GET     | `/api/v1/meetups`                     | Fetch all meetup records                          |
| POST    | `/api/v1/questions`                   | Create a question for a specific Meetup           |
| POST    | `/api/v1/meetups/<int:id>/rsvps`      | Respond to meetup RSVP                            |
| PATCH   | `/api/v1/questions/<int:id>/upvote`   | Upvote(increase votes by 1) a specific question   |
| PATCH   | `/api/v1/questions/<int:id>/downvote` | downvote(decrease votes by 1) a specific question |

## Running the tests

* Run `pytest --cov=app`

## Deployment

* The API is deployed [here](https://meetup-query-api.herokuapp.com/) on heroku

## Built With

* [Flask](http://flask.pocoo.org) - The web framework used

## Versioning

* This is version 1(v1) of the API which uses data structures to handle user data 

## Authors

### Bill Kariri

* Initial work : [Bill Kariri](https://github.com/BILLthebuilder)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* _nbo-36 team3_(Pre-bootcamp)
* _the-marines-nbo_(Bootcamp)
* Hat tip to anyone whose code was used
