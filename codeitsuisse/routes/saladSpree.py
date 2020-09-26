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
    results = []
    for i in range(len(myLists)):
        salad_prices = myLists[i]
        temp_res = prices(num, salad_prices)
        if temp_res != -1:
            results.append(temp_res)
        results.sort()

    if results == []:
        return 0
    else:
        return results[0]


def prices(num, price_list):
    tots = []
    counter = num
    for i in range(len(price_list) - counter):
        HasX = False
        for j in range(counter):
            if price_list[i + j] == "X":
                HasX = True
                break
        if HasX == False:   
            price = 0
            for j in range(counter):
                price += int(price_list[i+j])
            tots.append(price)

    tots.sort()
    if tots == []:
        return -1
    else:
        return tots[0]