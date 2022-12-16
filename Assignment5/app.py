from flask import Flask, jsonify, render_template, request, Response
import json

app = Flask(__name__)
jData = json.loads(open('./restaurants.json').read())
data=jData["Restaurants"]

@app.route('/', methods =['GET'])
def route_main():
    return "Welcome to the List of Restaurants"

@app.route('/restaurants/', methods =['GET'])
def restaurants_all():
    return render_template("index.html",items=data)

@app.route('/restaurants/<string:id>/', methods =['GET'])
def restaurants_by_id(id=''):
    myList=[]
    for element in data:
        if element["id"] == id:
            myList.append(element)
    return render_template("index.html",items=myList)

@app.route('/restaurants/<string:rating_id>/', methods =['GET'])
def resaturants_by_rating(rating_id=''):
    myList=[]
    for element in data:
        if element["id"] == rating_id:
            myList.append(element)
    return render_template("index.html",items=myList)
        

@app.route('/restaurants/type/<string:type_of_food>/', methods =['GET'])
def restaurants_by_type(type_of_food=''):
    myList=[]
    for element in data:
        if element["type_of_food"].lower() == type_of_food.lower():
            myList.append(element)
    return render_template("index.html",items=myList)

if __name__== "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0.", port=5000)
