from pymongo import MongoClient

from api.config_data.config import load_config
from api.config_data.dirs import DIR_REPO

conf = load_config(str(DIR_REPO / ".env"))


client: MongoClient = MongoClient(conf.mongo.db_url)

db = client[conf.mongo.db_name]

collection = db[conf.mongo.db_col]
