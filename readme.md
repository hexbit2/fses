## Flask App To Demostrate Session Based Auth
### Using Flask-Login

### Application Run Instructions

* article [link](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login) 

```
python -m venv venv
```

```
# From fses folder
export FLASK_APP=proj
export FLASK_DEBUG=1

flask run
```

#### Add DB objects
```
# Inside Python Terminal
from project import db, create_app, models
db.create_all(app=create_app()) # pass the create_app result so Flask-SQLAlchemy gets the configuration.
```

