from app import app
from flask import render_template
from flask import request

from app import fetch_data

@app.route('/')
@app.route('/index')
def index():
    return render_template("home.html")

# Return all the galaxies
@app.route('/api/v1/galaxy/all', methods=['GET'])
def api_v1_galaxy_all():
    """
    No parameter expected
    :return: list, return all galaxies with messiers for each galaxy
    """
    return fetch_data.all_data()
    # return 'a'
# Return information about one galaxy
@app.route("/api/v1/endpoint/", methods=['GET'])
def api_v1_galaxy_endpoint():
    print(request.headers['your-header-name'])
    return val


# Return information about one galaxy
@app.route("/api/v1/batch/", methods=['GET'])
def api_v1_galaxy_batch():
    data = request.get_json()
    print(data)
    if data is None:
        return 'Error, expected data'
    return data
