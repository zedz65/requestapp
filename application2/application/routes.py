from application import app
from flask import request, Response
# response is important to get a response
#normally import render template etc but not needed here as we dont use html
from random import randint
#specify 2 numbers and it picks a random int between the 2




@app.route('/animal/name', methods = ['GET']
# animal route which returns name of animal. method is GET. will access this route via app1
def animal_name():
    animals = ['cat', 'dog', 'cow']
# list of animals we will pick at random using randint
    return Response(animals[randint(0,2)], mimetype='text/plain')
#random 0,2 will pick a random number between 0 and 2 and output the item at that index in the list
#mime type specifies text json etc




@app.route('/animal/noise', methods = ['POST'])
#so we know which animal noise to return we use post method because
#it returns something after something sent according to what is sent it will 
def animal_noise():
    animal = request.data.decode
#data that gets sent comes in request.data.decode we set it to animal variable
#when we make a post request from other application it refers to this request
#comes as data and decode so we can see it as plain text

    if animal == "cat":
        noise = "meow"
    elif animal == "dog":
        noise = "woof"
    elif animal = "cow":
        noise = "moo"
    else:
        noise = "we dont know the noise for this animal"
     return Response(noise, mimetype='text/plain'
#basic if else if. note else is just a contingency incase wrong input
