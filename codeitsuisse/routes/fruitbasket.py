import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/fruitbasket', methods=['POST'])
def evaluate():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    apple = data.get("maApple");
    watermelon = data.get("maWatermelon");
    banana = data.get("maBanana");
    result = guess(apple, watermelon, banana)
    logging.info("My result :{}".format(result))
    return jsonify(result);

def guess(apple, watermelon, banana):
    Wa = 10
    Ww = 20
    Wb = 20
    return Wa*apple + Ww*watermelon + Wb*banana
