# Welcome program
## Overview
This little greeting program is based on a flask.  
The idea is simple: on the home page you're asked to enter the user's details,  
and then you're greeted, and depending on whether  
user has been to the site before, the answers may vary.
## Requirements
All requirements are specified in the requirements.txt file.  
You can install it via command `pip install -r requirements.txt`
## Installation
- Install all requirements
- export FLASK_APP env variable via command `export FLASK_APP=main` 
It may vary, depending on the OS
- Init db via command `flask init_db`
- Run flask app via command `flask run`
## CLI commands
After exporting FLASK_APP env variable you can use two cli command:  
- `flask init_db`
- `flask drop_db`
