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

    weights = {'maApple': 0, 'maWatermelon': 0, 'maBanana': 0, 'maPineapple': 0, \
                 'maAvocado': 0, 'maPomegranate': 0, 'maRamubutan': 0}
    fruits = []
    nums = []
    weights = []
    for k, v in d.items():
        fruits.append(k)
        nums.append(v)
    
    a = data.get('maApple')
    w = data.get('maWatermelon')
    b = data.get('maBanana')
    p = data.get('maPineapple')
    av = data.get('maAvocado')
    po = data.get('maPomegranate')
    r = data.get('maRamubutan')

    ans = 0
    for i in range(3):
        ans += nums[i]*weights.get(fruits[i])

    return str(ans)
