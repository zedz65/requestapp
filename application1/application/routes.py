from flask import render_template
from application import app
import requests

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', title='Home')

# basic home page route. specified as get even though it is defaulted




@app.route('/get/animal', methods = ['GET', 'POST'])
#going to get and post on this route
def animal():
    animal = requests.get('http://application2:5001/animal/name'
    noise = requests.post('http://application2:5001/animal/noise', data=animal.text)
    return render_template('animals.html', title='Animals', animal=animal.text, noise=noise.text)
#first we need to get the animal from the api when we get the request we store it in animal. makes sense
#animal variable requests get container name and then port because we cant access local host in docker.  
#going to route animal/name

#noise comment
#send the animal to a different route in the same application to get back the noise
#we post to the same container but different route animal/noise
#data we have to add animal.text so it shows the text instead of the code.

#html return render using jinja 2
#return template called animals.html title is animals and the parse 2 variables animal and noise.text to get text
#animal var holds animaltext and noise holds noisetext
