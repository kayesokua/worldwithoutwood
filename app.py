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
            'content': '',
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
            'title': 'Xylitol (Gum)',
            'content': 'BioLIB is a project aiming to enhance electric vehicle battery housings by combining wood and steel to achieve better temperature management, crash performance, vibration damping, thermal containment, cost-effectiveness, and a reduced ecological footprint.',
            'source': 'https://www.tugraz.at/projekte/biolib/home/'
        },
        {
            'image_url':'https://source.unsplash.com/random/?wood',
            'title': 'Laminated Veneer Lumber',
            'content': 'BioLIB is a project aiming to enhance electric vehicle battery housings by combining wood and steel to achieve better temperature management, crash performance, vibration damping, thermal containment, cost-effectiveness, and a reduced ecological footprint.',
            'source': 'https://www.tugraz.at/projekte/biolib/home/'
        },
        {
            'image_url':'https://source.unsplash.com/random/?wood',
            'title': 'Computer Chips',
            'content': 'These chips work just like traditional chips, but they use a different material for their base layer. Instead of silicon, they use cellulose nanofibril (CNF), a flexible and biodegradable material made from wood. This means that the chips can decompose in nature, which is a big improvement over traditional chips, which can take hundreds of years to break down.',
            'source': 'https://www.nature.com/articles/ncomms8170'
        },

        

        
    ]
    return render_template('index.html', utc_dt=datetime.datetime.utcnow(), catalog=catalog)

@app.route('/credits')
def credits():
    resources = [
        {
            "title": "Papers about Xylitol",
            "media": "sciencedirect.com",
            "url": "https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/xylitol"
        },
        {
            "title": "Papers about Lyocell Fiber",
            "media": "sciencedirect.com",
            "url": "https://www.sciencedirect.com/topics/engineering/lyocell-fiber"
        },
        {
            "title": "Biobased Multifunctional Laminates in Batteryhousings by Graz University of Technology",
            "media": "tugraz.at",
            "url": "https://www.tugraz.at/projekte/biolib/home"
        },
        {
            "title": "A newspaper lying over magazine by @ashni_ahlawat",
            "media": "unsplash.com",
            "url": "https://unsplash.com/@ashni_ahlawat"
        },
        {
            "title": "The benefits of modern method of construction based on wood in the context of sustainability",
            "media": "International Journal of Environmental Science and Technology",
            "url": "https://link.springer.com/article/10.1007/s13762-017-1282-6 "
        },
        {
            "title": "The benefits of modern method of construction based on wood in the context of sustainability",
            "media": "International Journal of Environmental Science and Technology",
            "url": "https://www.researchgate.net/profile/Elias-Hurmekoski-2/publication/291358292_Long-term_outlook_for_wood_construction_in_Europe/links/56a529cb08ae232fb207978e/Long-term-outlook-for-wood-construction-in-Europe.pdf "
        },
        {
            "title": "The benefits of modern method of construction based on wood in the context of sustainability",
            "media": "International Journal of Environmental Science and Technology",
            "url": "https://link.springer.com/article/10.1007/s13762-017-1282-6 "
        },
        {
            "title": "The benefits of modern method of construction based on wood in the context of sustainability",
            "media": "International Journal of Environmental Science and Technology",
            "url": "https://www.researchgate.net/profile/Elias-Hurmekoski-2/publication/291358292_Long-term_outlook_for_wood_construction_in_Europe/links/56a529cb08ae232fb207978e/Long-term-outlook-for-wood-construction-in-Europe.pdf"
        },
        {
            "title": "Circular economy in wood construction",
            "media": "Construction and Building Materials",
            "url": "https://www.sciencedirect.com/science/article/pii/S0950061822018827"
        },
        {
            "title": "High-performance green flexible electronics based on biodegradable cellulose nanofibril paper",
            "media": "International Journal of Environmental Science and Technology",
            "url": "https://www.nature.com/articles/ncomms8170"
        },





        




    ]
    return render_template('credits.html', utc_dt=datetime.datetime.utcnow(), title="Credits", resources=resources)