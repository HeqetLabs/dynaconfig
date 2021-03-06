from flask import Flask
from flask_rethinkdb import RethinkDB
from flask.ext import restful

app = Flask(__name__)
app.config["RETHINKDB_DB"] = "dynaconfig"

api = restful.Api(app)
db = RethinkDB()
db.init_app(app)


from dynaconfig.endpoints import Config, RevertConfig
api.add_resource(RevertConfig, "/config/revert/<int:user_id>/<string:config_name>/<int:version>")
api.add_resource(Config, "/config/<int:user_id>/<string:config_name>")
