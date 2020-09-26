import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/salad-spree', methods=['POST'])

def evaluateSalad():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    #inputValue = data.get("input");
    result = price(data.get("number_of_salads"), data.get("salad_prices_street_map"))
    logging.info("My result :{}".format(result))
    return jsonify(result);

def price(number_of_salads, salad_prices_street_map):
    result=0
    for street in salad_prices_street_map:
        if len(street)<=number_of_salads:
            continue
        else:
            for i in range(len(street)-number_of_salads+1):
                test=street[i:i+number_of_salads]
                if "X" in test:
                    continue
                else:
                    for i in range(number_of_salads):
                        test[i]=int(test[i])
                    if sum(test)< result or result==0:
                        result=sum(test)
    return {"result":result}
