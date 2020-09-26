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
    result = salad(data.get("number_of_salads"), data.get("salad_prices_street_map"))
    logging.info("My result :{}".format(result))
    return jsonify(result);

def salad(num, myLists):
    res = 0
    for i in range(len(myLists)):
        salad_prices = myLists[i]
        temp_res = prices(num, salad_prices)
        res = temp_res if temp_res > res else res
    return res

def prices(num, price_list):
    tot = 0
    counter = num
    for i in range(len(price_list)):
        if price_list[i] == "X":
            tot = 0 
            counter = num
        else:
            tot += price_list[i]
            counter -= 1
            if counter == 0:
                break
        if counter == 0:
            ans = tot
        else:
            ans = 0
    return ans