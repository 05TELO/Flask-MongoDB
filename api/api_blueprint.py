from bson import ObjectId
from flask import Blueprint
from flask import jsonify
from flask import request

from api.crud import serialized_alarm
from api.db import collection
from api.schemas import Alarm

api_blueprint = Blueprint("api", __name__)

@api_blueprint.route("", methods=["GET"])
def healthcheck():
    return jsonify({"message": "OK"})

@api_blueprint.route("/alarms", methods=["GET"])
def get_items():
    alarms = collection.find()
    res = list(map(serialized_alarm, alarms))
    return jsonify(res)


@api_blueprint.route("/alarms", methods=["POST"])
def create_item():
    alarm = Alarm(**request.json)
    result = collection.insert_one(alarm.model_dump())
    return jsonify({"id": str(result.inserted_id)})


@api_blueprint.route("/alarms/<alarm_id>", methods=["GET"])
def get_item(alarm_id):
    alarm = collection.find_one({"_id": ObjectId(alarm_id)})
    if not alarm:
        return not_found()
    return jsonify(serialized_alarm(alarm))


@api_blueprint.route("/alarms/<alarm_id>", methods=["PUT"])
def update_item(alarm_id):
    alarm = Alarm(**request.json)
    result = collection.update_one(
        {"_id": ObjectId(alarm_id)}, {"$set": alarm.model_dump()}
    )
    if result.modified_count == 0:
        return not_found()
    return jsonify({"Modified alarm count": result.modified_count})


@api_blueprint.route("/alarms/<alarm_id>", methods=["DELETE"])
def delete_item(alarm_id):
    result = collection.delete_one({"_id": ObjectId(alarm_id)})
    if not result:
        return not_found()
    return jsonify({"Deleted alarms count": result.deleted_count})


@api_blueprint.errorhandler(404)
def not_found(error=None):
    message = {"status": 404, "message": "Alarm not found"}
    resp = jsonify(message)
    resp.status_code = 404
    return resp



