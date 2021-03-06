## AWeber - Code Sample - Widget REST API

#### Write a CRUD REST API using Python for a single resource type. You may use a framework

#### The application must satisfy these requirements:
+ Written in Python 3.8 or later.
+ Endpoints to create, read, list, update, and delete objects called "Widgets"
+ Widget objects include the following properties (at least):
  + Name (utf8 string, limited to 64 chars)
  + Number of parts (integer)
  + Created date (date, automatically set)
  + Updated date (date, automatically set)
+ Widgets are persisted to and retrieved from a SQLite file database.
+ Include a README that describes how to setup and run the application.

#### Ideas to make the project even better:
- [X] Include unit or functional test coverage
- [X] Include an OpenAPI spec
- [X] PEP8 compliance
- [X] Pass standard lint tests (ie: flake8 or similar)
- [ ] Pass bandit security analysis
- [ ] Use Python type annotations

### Setup and Use
#### Initialize
```
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirments.txt
python3 init_db.py
```
#### Test
```pytest --disable-pytest-warnings```
#### Run
```python3 server.py```
