
def sql_to_json(obj, keys):
    jsonify = dict((x[0],dict(zip(keys[1:], x[1:]))) for x in obj )
    return jsonify