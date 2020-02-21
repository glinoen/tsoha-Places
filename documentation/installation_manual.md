# Setup guide
First clone the project, run
```
$ git clone https://github.com/glinoen/tsoha-Places.git
```
## Local use
Create virtual environment
```
$ python3 -m venv venv
```
Activate virtual environment
```
$ source venv/bin/activate
```
Install requirements
```
$ pip install -r requirements.txt
```
Run the program
```
$ python3 run.py
```
Enter the following address to your browser
```
$ localhost:5000
```
## Heroku
A 'Procfile' is included in the repo to help config heroku

### Deployment
You need to have a Heroku account and Heroku CLI installed.

Create a Heroku app by running
```
$ heroku create <app name>
```
Add a Postgre-addon for Heroku
```
$ heroku addons:create heroku-postgresql:hobby-dev
Deploy the current version of the application, run
```
$ git push heroku master
```
