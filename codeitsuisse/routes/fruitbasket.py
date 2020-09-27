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


def check(fruit):
    if fruit is None:
        return 0

def guess(data):
    
    data = dict(data)
    
    a = data.get('maApple')
    w = data.get('maWatermelon')
    b = data.get('maBanana')
    p = data.get('maPineapple')
    av = data.get('maAvocado')
    po = data.get('maPomegranate')
    r = data.get('maRamubutan')

    a = check(a)
    w = check(w)
    b = check(b)
    p = check(p)
    av = check(av)
    po = check(po)
    r = check(r)

    print(type(r))
    
    Wa = 0
    Ww = 0
    Wb = 0
    Wp = 0
    Wav = 0
    Wpo = 0
    Wr = 0
    ans = Wa*a + Ww*w + Wb*b + Wp*p + Wav*av + Wpo*po + Wr*r
    return str(ans)
