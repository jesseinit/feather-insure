# Feather API

A small insurance recommendation API

## Base URL

https://feather-rec-api.herokuapp.com

> Admin interface is available [here](https://feather-rec-api.herokuapp.com/admin). I havent at this time added a seed file to auto populate some tables required for the app to work optimally but it has been done on this deployed instance and accessible at the link above.

## API Documentation

[Postman Documentation](https://documenter.getpostman.com/view/7875106/TVsxB6ho)

## Setup

To get the application running on your local environment, run the following commands

- Create a directory (e.g feather-insure) and cd into it
- Run `git clone https://github.com/jesseinit/feather-insure.git .` to pull the code from Github to your machine
- Create a `.env` file populating it with actual values using the structure in the `.env.sample` file
- Ensure that you have created a database for development and test environments
- Install Docker and Docker Compose.
- Activate virtual environment with `python3 -m venv venv`
- Install application dependencies with `pip install -r requirements.txt`

## Starting the API

> Local Setup

```sh
- $ python manage.py db upgrade
- $ python manage.py runserver
OR
- $ make dev - if you are on mac or linux
```

> Docker

```sh
- $ docker-compose up --build - to start the api
- $ docker-compose down - to stop the api
```

## Built With

- [Flask](https://palletsprojects.com/p/flask/) - The fast and light-weight python micro-framework
- [PostgreSQL](https://www.postgresql.org/) - A production-ready relational database system emphasizing extensibility and technical standards compliance.
- [Redis](https://redis.io/) - Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache, and message broker.
- [Docker](https://www.docker.com/) - Docker is a service products that uses OS-level virtualization to deliver software in packages called containers.

## Authors

- **Jesse Egbosionu**
