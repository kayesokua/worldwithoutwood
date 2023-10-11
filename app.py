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
            'source': 'https://www.tis-gdv.de/tis/ware/papier/zeitung/zeitung-htm/'
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
            'image_url': 'https://www.tugraz.at/fileadmin/user_upload/tugrazExternal/8c980dc9-7c6f-4a5b-b72f-e7450816135d/images/Abbildungen/Concept.png',
            'title': 'Battery Housings',
            'content': 'BioLIB is a project aiming to enhance electric vehicle battery housings by combining wood and steel to achieve better temperature management, crash performance, vibration damping, thermal containment, cost-effectiveness, and a reduced ecological footprint.',
            'source': 'https://www.tugraz.at/projekte/biolib/home/'
        },
        {
            'image_url': 'https://images.unsplash.com/photo-1638028928694-2e683c5278a7?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2980&q=80',
            'title': 'Xylitol (Gum)',
            'content': 'Xylitol, also known as birch sugar, is produced through a chemical transformation of sugar alcohols.',
            'source': 'www.sciencedirect.com'
        },
        {
            'image_url':'https://source.unsplash.com/random/?computer,chips',
            'title': 'Computer Chips',
            'content': 'These chips work just like traditional chips, but they use a different material for their base layer. Instead of silicon, they use cellulose nanofibril (CNF), a flexible and biodegradable material made from wood. This means that the chips can decompose in nature, which is a big improvement over traditional chips, which can take hundreds of years to break down.',
            'source': 'https://www.nature.com/articles/ncomms8170'
        },
        {
            'image_url':'https://en.wikipedia.org/wiki/File:Laminated_Veneer_Lumber.png',
            'title': 'Laminated Veneer Lumber',
            'content': 'Laminated veneer lumber (LVL) is significant in construction due to its superior strength and stability, which makes it a versatile and reliable material for various structural applications. Additionally, LVL use of smaller, fast-growing trees and efficient manufacturing processes contributes to sustainability and reduces the demand for large timber resources.',
            'source': 'steico.com'
        }

   
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
            "title": "Circular economy in wood construction",
            "media": "Construction and Building Materials",
            "url": "https://www.sciencedirect.com/science/article/pii/S0950061822018827"
        },
        {
            "title": "High-performance green flexible electronics based on biodegradable cellulose nanofibril paper",
            "media": "International Journal of Environmental Science and Technology",
            "url": "https://www.nature.com/articles/ncomms8170"
        },
        
        {
            "title":  "Facts about Paper",
            "media": "f-mp.de",
            "url": "https://www.f-mp.de/res/expertenteam-papier/Papierherstellung.pdf"
        },
        {
            "title": "Facts about Paper",
            "media": "tis-gdv.de",
            "url": "https://www.tis-gdv.de/tis/ware/papier/zeitung/zeitung-htm/"
        },
        {
            "title": "Market share of Wood",
            "media": "Statista.com",
            "url": "https://www.statista.com/outlook/io/manufacturing/material-products/wood/worldwide"
        },
        {
            "title": "STEICO LVL laminated veneer lumber",
            "media": "STEICO LVL",
            "url": "https://www.steico.com/en/solutions/product-advantages/lvl-laminated-veneer-lumber"
        },


        

    ]
    return render_template('credits.html', utc_dt=datetime.datetime.utcnow(), title="Credits", resources=resources)