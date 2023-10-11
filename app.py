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
            'title': 'Lyocell for Textiles',
            'content': 'Lyocel is another type of regenerated cellulose fiber made from wood pulp. It is significant for eco-friendly manufacturing, reducing water and chemical usage. This sustainable fabric offers comfort and freshness, making it ideal for eco-conscious clothing.',
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
            'image_url':'https://source.unsplash.com/random/?laminated,wood',
            'title': 'Laminated Veneer Lumber',
            'content': 'Laminated veneer lumber (LVL) is significant in construction due to its superior strength and stability, which makes it a versatile and reliable material for various structural applications. Additionally, LVL use of smaller, fast-growing trees and efficient manufacturing processes contributes to sustainability and reduces the demand for large timber resources.',
            'source': 'steico.com'
        },
        {
            'image_url':'https://source.unsplash.com/random/?vehicle',
            'title': 'Structural Vehicle Components',
            'content': 'The use of wood in the automotive industry offers several advantages, including lightweight construction for enhanced energy efficiency, sustainability with a lower carbon footprint, and improved interior acoustics for a quieter driving experience. Wood also provides design flexibility and a natural aesthetic, along with potential for biocomposites to enhance strength and reduce waste. While this application is still in development, it holds promise as the automotive industry seeks more eco-friendly and sustainable solutions in the future.',
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
        {
            "title": "Wood As A Technical Material For Structural Vehicle Components",
            "media": "ScienceDirect.com",
            "url": "https://pdf.sciencedirectassets.com/282173/1-s2.0-S2212827116X00030/1-s2.0-S2212827116001487/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIE%2B5TxRKXQ0bbNrPDDxckineOIBpkD5L%2BCtK0GFAHdE%2BAiBtZSbj3H8vCvfZY%2BZtz8U%2FGwQDVl7N0PM0igCRwJrxTiq8BQjq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAUaDDA1OTAwMzU0Njg2NSIMxA5CR0Eq3%2B4BUYY1KpAFpUUXFZ0fVBxUL8siR%2FwJtIP4iH0j%2Fop5v7Uzi80KonAHbEnl3uhdfJCRIijCxZVfHPh5Qn0z4e8cWjlLx7%2F467lCPHDz75MdkNIyEInGtMgBFM%2FAJgf9%2FyT%2BNJI4wj9owhdW%2Bww8jxEeon%2BfJApoVuEkx%2Ff%2BiX5Ksp5ZzaEWZCUuO11G34IwWjUib6K163OntKCq6N4bifvXOrdOGOiaX3EAyGa3WTDPa5MNEZ15MRXsC2uZlBUGVQPyDelhrRC%2BkBw6Ys47cBZ3gbsMGnT6bf2trpQq4vmdH6%2FuP9BdBflqMHCtEJSmPFJM%2BBSwRtpa3dKWbw%2BOXsqtGoHjCnzHoyPfps48f6Lv4jfihN6UDO2eSpwSflpCNrBlEAXiGnVmoqKCvK3docIUCVHTUDm%2Btc1EAYmBOjJY2UeoOOHV%2BUcsEQ6cOti5Rn1Nj%2Fn6O7Ncz3FOstNnhKvdWtlnbwaPdxIrEU304vGhkHS2zT%2BsYMTz1s7ZXaI13XaIFIDBAzOcje0BMfGigBz7Ureg5EbxTT2Rzw2P1e2Ax0A2jIh2xdmSmmJ6M4YrpDAZBNVjkI%2BnBJBFZOWNV1b60ZBPejjLcBZtGf2W2puWKPAHeM6vntGsQRVgCrLEostZMhbDCSNOvcEP6iK8YjOyKmoRniAjTK%2F0Nvt8THvzR9tQltf%2FF38Dw3iVmw1ZQiH7xlsQyguWnXpBErbJZMOAoYnetWiGvplf4T6KWiEozCeOFdsb3B%2FJCbv1Xb2XSyH241BqIl%2FszoYE6CYj%2BiCkyzK6APQpxvxd%2BJGDnUTXiixox7ZNk2nMi9GhvfUaTn2e97fPFIeDSLgXvsBkEgXh9jfLJ44inxf9hMCkTchDRLCCAa5mw2wwnbeZqQY6sgFi7h0HJaaecNW%2B%2BYykJrpepViB6y0YWAYzbWyge4oie%2Bgpn4XJjE1tAW%2BxlbfByIiW5MiSMjS88g9fE9DE7X%2BhdcYKZntDAc3dwrXkOrYcGbJUl2vgg7G0%2F%2BtphPUADU21XQIObAWs%2F10R4suG%2BkB5YIbP7%2B2BRPN4seLMX%2Fs%2BtUlQ9%2FY%2Frbc6rUm253I8%2BaELBVDLWXCDljbObZGJSccgdcVLj3YV9egELi1L40Mb%2F%2Fnx&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231011T085618Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTYXDAV3WOR%2F20231011%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=4f58f5d177b8540efc2619c5fd811af5ce8bb1e3baaa13fa3eb23dec5767c2f5&hash=f036642f0082d300dc0724937b5bbed2caeb3d11b4d25e37cfa0adc3c3a15e7b&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S2212827116001487&tid=spdf-5bce86ff-2039-4f66-9332-619687e0c220&sid=8530bd385c862546484946c7e1988de026acgxrqb&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=1b115c525b510a505c53&rr=8145e396d9175b49&cc=at"
        },


        

    ]
    return render_template('credits.html', utc_dt=datetime.datetime.utcnow(), title="Credits", resources=resources)