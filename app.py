import datetime
from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def index():
    catalog = [
        {
            'image_url': 'static/assets/images/ashni-ePWaAwUn80k-unsplash.jpg',
            'title': 'Paper',
            'content': 'Wood has been used to make paper for centuries, but it became more common in the 19th century with the invention of the wood pulp papermaking process.',
            'source': ''
        },
        {
            'image_url': 'https://lyocell.info/images/lyocell-outfit.jpeg',
            'title': 'Lyocell for Sportswear',
            'content': 'Lyocel use of wood pulp is significant for eco-friendly manufacturing, reducing water and chemical usage. This sustainable fabric offers comfort and freshness, making it ideal for eco-conscious clothing.',
            'source': 'https://www.sciencedirect.com/topics/engineering/lyocell-fiber'
        },
        {
            'image_url': 'https://i.insider.com/57b476b5db5ce963008b7305?width=600&format=jpeg&auto=webp',
            'title': 'Transparent Wood',
            'content': 'Multi-stage chemical process starts with slicing wood, treating wood chips to remove lignin for opacity, immersing in a clear polymer (e.g., PEG), drying to form transparent wood. Process specifics vary by manufacturing method.',
            'source': 'University of Maryland Energy Research Center'
        },
        {
            'image_url': 'assets/images/shutterstock-1369448567.jpg',
            'title': 'Lightweight Cars',
            'content': 'Wood has been used to make paper for centuries...',
            'source': ''
        },
        {
            'image_url': 'assets/images/shutterstock-1369448567.jpg',
            'title': 'Battery Housings',
            'content': 'Wood has been used to make paper for centuries...',
            'source': ''
        },
        {
            'image_url': 'assets/images/shutterstock-1369448567.jpg',
            'title': 'Gum',
            'content': 'BioLIB is a project aiming to enhance electric vehicle battery housings by combining wood and steel to achieve better temperature management, crash performance, vibration damping, thermal containment, cost-effectiveness, and a reduced ecological footprint.',
            'source': 'https://www.tugraz.at/projekte/biolib/home/'
        },
        {
            'image_url':'https://source.unsplash.com/random/?wood',
            'title': 'Laminated Veneer Lumber',
            'content': 'BioLIB is a project aiming to enhance electric vehicle battery housings by combining wood and steel to achieve better temperature management, crash performance, vibration damping, thermal containment, cost-effectiveness, and a reduced ecological footprint.',
            'source': 'https://www.tugraz.at/projekte/biolib/home/'
            
        }

        
    ]
    return render_template('index.html', utc_dt=datetime.datetime.utcnow(), catalog=catalog)

@app.route('/credits')
def credits():
    return render_template('credits.html', utc_dt=datetime.datetime.utcnow(), title="Credits")