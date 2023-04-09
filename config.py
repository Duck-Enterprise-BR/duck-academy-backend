from pydantic import BaseSettings
import json

env_file = open('env.json')
data = json.load(env_file)

class Settings():
    db_user = data['db_user']
    db_password = data['db_password']
    db_database = data['db_database']
    db_host = data['db_host']
    db_port = data['db_port']
    access_token = data["access_token"]