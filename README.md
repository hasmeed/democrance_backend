# Democrance API Coding test


## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/hasmeed/democrance_backend.git
$ cd democrance_backend
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv --no-site-packages env
$ source env/bin/activate
```
Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000`

## Postman API Doc

Before you start interracting with the app. kindly check the link below for the 
Postman API documentation to have a better understanding of the endpoints provided into the application 

`https://documenter.getpostman.com/view/12073690/UVeFP7eA`

## Admin Page 

you can login into the admin by vising `http://127.0.0.1:8000/admin`
username: admin 
password: monalisa

## Tests

To run the tests, `cd` into the directory where `manage.py` is:
```sh
(env)$ python manage.py test 
```

## Future Enhancements

- As time goes on, there might be need to dockerize this app to allow easy and seamless deployment across different platforms

- We could also add authentication app to support customer login and signup as well as authorization 

- We can also breakdown some of the apps into smaller module as the requirements grows in features
