def serialized_alarm(alarm):
    alarm["_id"] = str(alarm["_id"])
    return alarm
