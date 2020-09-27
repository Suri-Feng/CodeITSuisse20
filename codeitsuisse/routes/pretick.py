import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/pre-tick', methods=['POST'])
def evaluatePretick():
    data = request.get_csv();
    logging.info("data sent for evaluation {}".format(data))
    print(type(data))
    result = "920"
    logging.info("My result :{}".format(result))
    return jsonify(result);



