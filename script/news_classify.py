import os
import sys
import cohere
from cohere.classify import Example

sys.path.append(os.path.abspath(os.path.join('..')))
import config
api_key = config.cohere_api['api_key']
co = cohere.Client(api_key)
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify({"status": "sucess"})

@app.route('/api/bnewscore', methods=['GET', 'POST'])
def classify_news():
    if request.method == "GET":
        pass
    elif request.method == "POST":
        response = co.classify(
            model='large',
            inputs=["The construction sector is expected to be boosted by riots and looting repairs"],
            examples=[
                Example("Boris Johnson using a taxpayer-funded jet for an election campaign fits a long history of taking things he didn\'t pay for","0"),
                Example("Stumbled across an interesting case, a woman facing eviction from the home that she inherited from her brother in 2007. Turns out her brother was in business with a notorious international criminal Paul Le Roux, who is currently serving 25 years in a New York prison.","1"),
                Example("Marché Résines dans les peintures et revêtements 2021 avec les données des meilleurs pays et l’analyse Covid-19, la portée future, l’estimation de la taille, les revenus, les tendances des prix et les prévisions d’ici 2026","2"),
                Example("AI drives data analytics surge, study finds", "3"),
                Example("7th Anniversary of SCOAN Collapse in Nigeria-SABC News", "4"),
            ],
        )
        print('The confidence levels of the labels are: {}'.format(response.classifications))
        return jsonify({"status": "sucess", "res": response.classifications[0]})



if __name__ == '__main__':
    port = int(os.environ.get("POST", 33507))
    app.run(host= '0.0.0.0', debug=True, port=port)
