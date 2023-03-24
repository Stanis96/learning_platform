[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
<h1 align="center">Learning platform</h1>

### Description:
* The Django application is configured to run the parser on a schedule using Celery and RabbitMQ.
The parser retrieves data from [Codeforces](https://codeforces.com/problemset?order=BY_SOLVED_DESC)
and stores it in a PostgreSQL database.
When new data is retrieved, it is either created as a new entry in the database or updated if it already exists.
* The Telegram bot is configured to access the database and get the latest cleared data.
Users can interact with the bot to search for specific tasks based on search filters.

### Installation:
* Clone the repository to a local directory:
  ```sh
  git clone https://github.com/Stanis96/learning_platform
  ```
* Set your own variable values in ```.env_template``` and rename to ```.env```
* Application launch:
```sh
  docker-compose -f docker-compose.yaml up --build
  ```
