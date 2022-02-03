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

## Walkthrough

Before you interact with the application, go to GoCardless Sandbox and set up
the Redirect URI in the Developer settings. To make it work with this
application, use the value `http://127.0.0.1:8000/gocardless/confirm/`. This is to
make sure you are redirected back to your site where the purchase is verified
after you have made a purchase.
## Tests

To run the tests, `cd` into the directory where `manage.py` is:
```sh
(env)$ python manage.py test 
```
