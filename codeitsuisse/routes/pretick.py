import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

import pandas as pd

logger = logging.getLogger(__name__)

@app.route('/pre-tick', methods=['POST'])
def evaluatePretick():
    #data = request.get_json();
    data = request.get_data();
    print(data)
    data = pd.read_csv();
    logging.info("data sent for evaluation {}".format(data))
    print(type(data))
    result = "920"
    logging.info("My result :{}".format(result))
    return jsonify(result);



