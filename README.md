# Shopping

[![Build Status](https://travis-ci.org/verenceLola/Shopping.svg?branch=develop)](https://travis-ci.org/verenceLola/Shopping)
[![Build Status](https://verencelola.visualstudio.com/Shopping%20List/_apis/build/status/verenceLola.Shopping?branchName=develop)](https://verencelola.visualstudio.com/Shopping%20List/_build/latest?definitionId=11&branchName=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/1a24177c6a8c5e330a97/maintainability)](https://codeclimate.com/github/verenceLola/Shopping/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/1a24177c6a8c5e330a97/test_coverage)](https://codeclimate.com/github/verenceLola/Shopping/test_coverage)
[![codecov](https://codecov.io/gh/verenceLola/Shopping/branch/develop/graph/badge.svg)](https://codecov.io/gh/verenceLola/Shopping)
[![Coverage Status](https://coveralls.io/repos/github/verenceLola/Shopping/badge.svg)](https://coveralls.io/github/verenceLola/Shopping)

Django backend for Shopping list application

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/1b71afb74d80f92b7cf2)

- The Application has been documented using Postman Documentation tht can be viewed [here.](https://documenter.getpostman.com/view/4146974/SVtSVp2J)

## Setting Up the Application Locally

### Installing Redis

- Redis is required by the application for the application to run. To use the local redis server, ensure you have redis [installed](https://redis.io/topics/quickstart) and running. Add the following to your .env file

    ``` bash
    REDIS_URL=redis://<username>:<password>@127.0.0.1:6379 #  redis://127.0.0.1:6379 if no username or password configured, or just a remote hosts URL
    ```

### Setup VirtulEnvironment

- Setup Pyhton virtual environment by running `python3 -m venv venv`

- Activate the virtual environment by running `source venv/bin/activate`

### Install Application Dependencies

- Run the following command to install application dependencies `pip install -r requirements.txt`

- After installing the dependencies, add the necessary environmental variables required by the application. Sample environmental varials are:

    ```bash
    DEBUG=True
    DATABASE_URL=postgres://<user>:<password>@<host>:<port>/<database name>
    SECRET_KEY="611=df5*i4evgbpu3)$th%=##=kw#h#@8zomsn1$eo6f^uv74$" # sample SECRET_KEY
    PAGE_SIZE=20 # overide PAGE_SIZE, default 10
    ```

- Add the above variables in a file name `.env` in the root of the project

### Perform Initial Migrations

- To ensure that the database tables are properly configured, run migrations by running `./manage.py migrate` at the root of the project

### Start the Server

- After successfully performing migrations, the server can be started by running `./manage.py runserver` at the root of the project

### Running Tests

- To run unit test, [pytest](https://docs.pytest.org/en/latest/) is used. Run `pytest` at the root of the project

## Deployments and Releases

- The project had been deployed to Heroku. To view the various versions of the deployed apps, goto [here](https://github.com/verenceLola/Shopping/deployments)

- To view project releases, goto [releases](https://github.com/verenceLola/Shopping/releases)
