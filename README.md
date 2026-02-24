# Project Title
Compare generation of a Python client for a flask project.
## Description
Creating the client fully-manual, semi manual using code generation systems like
flask-smorest.
## Getting Started
### Dependencies
* python 3.10
### Installing
Software can be cloned from https://github.com/asburr/exemplar_flask.
### Executing program
Start server
```
cd projects/exempler_flask
poetry lock
poetry sync --with dev,inhouse_wsdev,inhouse_wsprod
poetry run flask --app exemplar_flask.flaskapp init-db
/home/andrew/miniconda3/bin/poetry run flask --app exemplar_flask.flaskapp run
```
Using the manually generated client
```
cd projects/exempler_flask
# lock and sync if not already done above.
poetry lock
poetry sync --with dev,inhouse_wsdev,inhouse_wsprod
./flaskclient.sh test post value1 value1.2
None
./flaskclient.sh test get value1
{'field1': 'value1', 'field2': 'value1.2', 'id': 1}
./flaskclient.sh test2 post value1 value2 value2.1
None
./flaskclient.sh test2 get value1 value2
{'field2': 'Tue, 24 Feb 2026 14:20:58 GMT', 'field3': 'value2', 'id': 1, 'test_id': 'value1'}
```
## openapi schema
Use the above procedures to start the server, then using curl to dump the
openapi schema into a file called openapi.json
```
# Start the server...see above.
curl http://127.0.0.1:5000/openapi.json > openapi.json
```
## openapi client
Using openapitools/openapi-generator-cli to generate a Python client.
```
cd projects/exempler_flask
./openapigen.sh
```
## openapipython client
Using openapi-python-client to generate a Python client.
```
cd projects/exempler_flask
./openapipythongen.sh
```
## Version History
* 0.1
  * Initial release
## License
This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details
      