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
    dataString = data.decode('utf-8')
    data = json.loads(dataString)
    
    a = data.get('maApple')
    w = data.get('maWatermelon')
    b = data.get('maBanana')
    p = data.get('maPineapple')
    av = data.get('maAvocado')
    po = data.get('maPomegranate')
    r = data.get('maRamubutan')

    print(data)
    a = 16
    b = 45
    c = 91
    Wa = 35
    Wb = 20
    Wc = 20
    ans = Wa*a + Wb*b + Wc*c
    return str(ans)
