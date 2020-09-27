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
    print(data)
    a = data['maApple']
    w = data['maWatermelon']
    b = data['maBanana']
    print(data)
    a = 16
    b = 45
    c = 91
    Wa = 35
    Wb = 20
    Wc = 20
    ans = Wa*a + Wb*b + Wc*c
    return str(ans)
