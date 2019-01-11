[![Build Status](https://travis-ci.org/BILLthebuilder/meetup-query.svg?branch=develop)](https://travis-ci.org/BILLthebuilder/meetup-query)
[![Coverage Status](https://coveralls.io/repos/github/BILLthebuilder/meetup-query/badge.svg?branch=develop)](https://coveralls.io/github/BILLthebuilder/meetup-query?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/fbc43151aa7a1cb8a6a0/maintainability)](https://codeclimate.com/github/BILLthebuilder/meetup-query/maintainability)


# meetup-query
A web application that crowd-sources questions for a meetup. 'meetup-query' helps the meetup organizer prioritize questions to be answered. Other users can vote on asked questions and they bubble to the top or bottom of the log.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
What things you need to install the software and how to install them
* Python 3.6.7
* Postman
### Installing
A step by step series of examples that tell you how to get a development env running
Say what the step will be
* Clone the project repository
`git clone git@github.com:BILLthebuilder/meetup-query.git`

* Change the directory
`cd meetup-query`

* Install the virtual environment
`virtualenv venv`

* Activate the virtual environment
`source/venv/bin/activate`

* Install the dependencies
`pip install -r requirements.txt`

* Run the application
    ```
      export FLASK_APP=run.py
      export FLASK_ENV=development
      export FLASK_DEBUG=1
      flask run
    ```
### The API Endpoints
| HTTP Verb  	|Endpoint   	|Function   	|
|---	|---	|---	|
| POST  	|`/api/v1/meetups`   	|Create a Meetup record   	|
| GET  	|`/api/v1/<meetup-id`   	|Fetch a Specific Meetup record   	|
| GET  	|`/api/v1/meetups/upcoming`   	|Fetch all upcoming meetup records   	|
| POST  	|`/api/v1/questions`   	|Create a question for a specific Meetup    	|
| POST  	|`/api/v1/meetups/<meetup-id/rsvps`   	|Respond to meetup RSVP   	|
| PATCH  	|`/api/v1/questions/<question-id>/upvote`   	|Upvote(increase votes by 1) a specific question   	|
| PATCH  	| `/api/v1/questions/<question-id>/downvote`  	|downvote(decrease votes by 1) a specific question    	|

## Running the tests
* Run `pytest --cov=app`

## Deployment
* The API is deployed [here](https://meetup-query-api.herokuapp.com/) on heroku

## Built With
* [Flask](http://flask.pocoo.org) - The web framework used

## Contributing
Please read this [code of conduct](http://bit.ly/honor-code2018) for details on Andela's honor code

## Versioning
* This is version 1(v1) of the API which uses data structures to handle user data 

## Authors
 **Bill Kariri** 
*  Initial work* 
*  [Bill Kariri](https://github.com/BILLthebuilder)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
* _NBO-36 TEAM3_
* Hat tip to anyone whose code was used
