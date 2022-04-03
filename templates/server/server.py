#from crypt import methods
from urllib import response
from flask import Flask, request, jsonify, redirect, url_for, render_template
import util
from util import get_orbit_names,get_launchsite_names,get__reused,get_Gridfins,get_landingpad,get_launch_prediction,get_legs,load_saved_artificates
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("app.html")


@app.route("/get_orbit_names",methods=['GET'])
def get_orbit_names():
    response=jsonify({
        "orbit":util.get_orbit_names()
    })
    response.headers.add("Access-Control-Allow-Origin","*")
    return response

@app.route("/get_Gridfins",methods=['GET'])
def get_Gridfins():
    response=jsonify({
        "Gridfins":util.get_Gridfins()
    })
    response.headers.add("Access-Control-Allow-Origin","*")
    return response

@app.route("/get_reused",methods=['GET'])
def get__reused():
    response=jsonify({
        "reused":util.get__reused()
    })
    response.headers.add("Access-Control-Allow-Origin","*")
    return response

@app.route("/get_legs",methods=['GET'])
def get_legs():
    response=jsonify({
        "legs":util.get_legs()
    })
    response.headers.add("Access-Control-Allow-Origin","*")
    return response

@app.route("/get_landingpad",methods=['GET'])
def get_landingpad():
    response=jsonify({
        "landingpad":util.get_landingpad()
    })
    response.headers.add("Access-Control-Allow-Origin","*")
    return response

@app.route("/get_launchsite_names",methods=['GET'])
def get_launchsite_names():
    response=jsonify({
        "launchsite":util.get_launchsite_names()
    })
    response.headers.add("Access-Control-Allow-Origin","*")
    return response


@app.route("/sub",methods=["GET","POST"])

def predict_launch():
    if request.method=="POST":
        payloadmass = int(request.form["payloadmass"])
        flights = float(request.form["flights"])
        Block = float (request.form["Block"])
        ReusedCount = float(request.form["ReusedCount"])
        orbit = request.form["orbit"]
        gridfins = request.form["gridfins"]
        reused = request.form["reused"]
        legs = request.form["legs"]
        landingpad = request.form["landingpad"]
        launchsite = request.form["launchsite"]

        return render_template("sub.html",prediction=get_launch_prediction(payloadmass,flights,Block,ReusedCount,orbit,gridfins,reused,legs,landingpad,launchsite))
  

if __name__=="__main__":
    print("Starting Python Flask server for Space Launch Prediction...")
    util.load_saved_artificates()
    app.run()