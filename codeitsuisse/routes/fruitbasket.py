import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/fruitbasket', methods=['POST'])

def evaluateFruitBasket():
    data = request.get_data();
    data = json.loads(data)
    logging.info("data sent for evaluation {}".format(data))
    result = guess(data)
    #result = 200
    logging.info("My result :{}".format(result))
    return jsonify(result);

def guess(data):
    apple = data["maApple"]
    watermelon = data["maWatermelon"]
    banana = data.get["maBanana"]
    Wa = 10
    Ww = 20
    Wb = 20
    ans = Wa*apple + Ww*watermelon + Wb*banana
    return str(0)
