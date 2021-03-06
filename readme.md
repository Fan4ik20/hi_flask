# Welcome program
## Overview
This little greeting program is based on a flask.  
The idea is simple: on the home page you're asked to enter the user's details,  
and then you're greeted, and depending on whether  
user has been to the site before, the answers may vary.
## Requirements
All requirements are specified in the requirements.txt file.  
You can install it via command `pip install -r requirements.txt`
## Installation. First launch
- Install all requirements
- export FLASK_APP env variable via command `export FLASK_APP=main` 
It may vary, depending on the OS
- Init db via command `flask init_db`
- Run flask app via command `flask run`  
Or you can start docker container via commands:
- `docker build --tag {your_tag} .`
- `docker start -d -p 5000:5000 --name {your_name} {your_tag}`
- `docker exec -t -i {your_tag} bash`
- `flask init_db`
- `exit`  
After these manipulations you can access the web app at `localhost:5000` url.
## CLI commands
After exporting FLASK_APP env variable you can use two cli command:  
- `flask init_db`
- `flask drop_db`
## Additional
You can  also provide your own postgresql database.  
To do this, specify .env file with these variables in the format `variable=value`:
- DB_HOST
- DATABASE
- DB_USER
- DB_PORT
- DB_PASSWORD
## Link
https://hi-flask.herokuapp.com
## License
MDI