# import app.fetch_data.web as wb

from app import app
import app.fetch_data.web as wb
from flask import render_template
from flask import request
from flask import jsonify


@app.route('/')
@app.route('/index')
def index():
    return render_template("home.html")


# Return information about one galaxy
@app.route("/api/v1/web", methods=['GET', 'POST'])
def api_v1_web():
    galaxy = request.args.get('galaxy', default=None)
    messier = request.args.get('messier', default=None)
    if messier is not None or galaxy is not None:
        res = wb.get_data(galaxy, messier)
        return jsonify(res)
    else:
        return "Expected at least one good parameter \n <br>" \
               "example /api/v1/web?messier=example1 \n <br>" \
               "example /api/v1/web?galaxy=example2 \n <br>" \
               "example /api/v1/web?messier=example1&galaxy=example2"


# Return information about one galaxy
@app.route("/api/v1/batch/", methods=['GET'])
def api_v1_batch():
    if request.headers['Content-Type'] == 'application/json':
        data = request.get_json()
        if data is None:
            return 'Error, expected data'
        return jsonify(data)
    else:
        return "Expected 'Content-Type': 'application/json' instead of 'Content-Type': '" + request.headers['Content-Type'] + "'"


# Return web page
@app.route("/galaxies", methods=['GET'])
def web_galaxies():
    #to do:handle args
    return render_template("galaxies.html")

# Return web page
@app.route("/messiers", methods=['GET'])
def web_messiers():
    #to do:handle args
    return render_template("messiers.html")

# Return web page
@app.route("/galaxies/<galaxy>", methods=['GET'])
def web_galaxy(galaxy):
    #to do:handle args
    return render_template("galaxy.html")

# Return web page
@app.route("/messiers/<messier>", methods=['GET'])
def web_messier(messier):
    #to do:handle args
    return render_template("messier.html")
