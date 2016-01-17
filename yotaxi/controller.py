from flask import request, render_template, Flask
from API_KEY import api_token
from API_KEY import google_key
import json
import requests

# Yo api end point url
YO_API = "https://api.justyo.co/yo/"
app = Flask(__name__)



def send_yo(username, link):
    """Yo a username"""
    requests.post(
        YO_API,
        data={'api_token': api_token, 'username': username, 'link': link})


@app.route('/')
def main():
    """Index Controller"""
    return render_template('index.html')


@app.errorhandler(404)
def handle_error(e):
    return render_template('404.html')


@app.route('/noresult')
def noresult():
    return render_template('noresult.html')

@app.route('/yo')
def yo():
    """Handle callback request"""
    username = request.args.get('username')
    location = request.args.get('location')
    splitted = location.split(';')
    # Parse latitude and longitude from request params
    latitude = splitted[0]
    longitude = splitted[1]
    if latitude is None:
        send_yo(username, 'http://www.google.com/teapot')
    else:
	link = "uber://?action=setPickup&pickup[latitude]={0}&pickup[longitude]={1}
	send_yo(username, link)
    return 'OK'

if __name__ == '__main__':
    app.run()
