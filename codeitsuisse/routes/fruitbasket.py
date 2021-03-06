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
    
    d = dict(data)

    weights = {'maApple': 3, 'maWatermelon': 52, 'maBanana': 0, 'maPineapple': 82, \
                 'maAvocado': 6, 'maPomegranate': 28, 'maRamubutan': 29}
    fruits = []
    nums = []
    for k, v in d.items():
        fruits.append(k)
        nums.append(v)

    ans = 0
    for i in range(3):
        ans += nums[i]*(weights.get(fruits[i]))

    return str(ans)
