# wttd-eventex
Main project of the course Welcome to the Django

[![Build Status](https://travis-ci.org/raphaelcmacedo/wttd-eventex.svg?branch=master)](https://travis-ci.org/raphaelcmacedo/wttd-eventex)
[![Code Health](https://landscape.io/github/raphaelcmacedo/wttd-eventex/master/landscape.svg?style=flat)](https://landscape.io/github/raphaelcmacedo/wttd-eventex/master)

## How to develop?

1. Clone the repository.
2. Create a virtualenv with Python 3.5
3. Activate virtualenv.
4. Install dependencies.
5. Configure the instance with the .env
6. Run the tests.

```console
git clone git@github.com:raphaelcmacedo/wttd-eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## How to deploy?

1. Create an instance in heroku.
2. Send the settings to the heroku.
3. Define a safe SECRET_KEY for instance.
4. Set DEBUG = False
5. Set the email service.
6. Send the code to the heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configuro o email
git push heroku master --force
```

