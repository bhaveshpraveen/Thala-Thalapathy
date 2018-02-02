# Thala-Thalapathy

A simple Django app that uses [Rethinkdb](https://rethinkdb.com/) to keep track of the votes cast by users and Django-Channels for real-time update

### Running locally
To run this locally you need Python, Redis, Rethinkdb
On mac you can install Redis and Rethinkdb using [Homebrew](https://brew.sh/)
```shell
brew update && brew install redis
```
```shell
brew update && brew install rethinkdb
```
- Install requirements: `pip install -r requirements`
- Start redis server in a separte terminal: `redis-server --port 7777` 
- Start the Rethinkdb server in a separte terminal: `rethinkdb`
- Start the Django application in a different terminal: `./manage.py runserver`

*****Note**:
The JS code is messy(Not a JS developer). Excuse my front-end skills.


### TODO:
Dockerize


### References:
1. https://channels.readthedocs.io/en/latest/getting-started.html
2. https://github.com/jacobian/channels-example
