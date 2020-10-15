Flaskr
======

The basic blog app built in the Flask [`tutorial`](http://flask.pocoo.org/docs/tutorial/).


Install
-------

To install

```
    # clone the repository
    $ git clone https://github.com/DiegoPiloni/flaskr.git
    $ cd flaskr
```


Create a virtualenv and activate it

```
    $ python3 -m venv venv
    $ source venv/bin/activate
```


Install Flaskr

```
    $ pip install -e .
```


Run
---

```
    $ export FLASK_APP=flaskr
    $ export FLASK_ENV=development
    $ flask init-db  # Create or clean the database
    $ flask run  # Start the server
```


Open http://127.0.0.1:5000 in a browser.

Register some users and check in DBeaver. `sqlite` database is located at `instance/flaskr.sqlite`


SQL injection
-------------

Register with [`Little Bobby Tables`](https://xkcd.com/327/) user:

```
    username: Robert', 'F'); DROP TABLE user; --
    password: *
```

After running this, the `user` table [no longer exists](https://www.picuki.com/media/2278427825370702453).

To continue using the app, run: `$ flask init-db`.

Not vulnerable code is commented in `register` view in `flaskr/auth.py`.


Test
----

```
    $ pip install '.[test]'
    $ pytest
```

Run with coverage report

```
    $ coverage run -m pytest
    $ coverage report
    $ coverage html  # open htmlcov/index.html in a browser
```
