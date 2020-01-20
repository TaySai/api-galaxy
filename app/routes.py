from app import app
from flask import render_template
from flask import request


@app.route('/')
@app.route('/index')
def index():
    return render_template("home.html")

# Return all the galaxies
@app.route('/api/v1/galaxy/all', methods=['GET'])
def api_v1_galaxy_all():
    return 'all galaxies'

# Return information about one galaxy
@app.route("/api/v1/galaxy/endpoint/<val>", methods=['GET'])
def api_v1_galaxy_endpoint(val):
    print('hello')
    return val


# Return information about one galaxy
@app.route("/api/v1/galaxies/batch/", methods=['GET'])
def api_v1_galaxy_batch():
    data = request.get_json()
    print(data)
    if data is None:
        return 'Error, expected data'
    return data