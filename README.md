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
```
Use the client
```
cd projects/exempler_flask
./flaskclient.sh
./flaskclient.sh test post value1 value1.2
```
## Help
Any advise for common problems or issues.
```
command to run if program contains helper info
```
## Version History
* 0.2
  * Various bug fixes and optimizations
  * See [commit change]() or See [release history]()
* 0.1
  * Initial Release
## License
This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details
      