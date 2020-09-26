import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/swaphedge', methods=['POST'])
def evaluateHedging():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    result = response(data)
    logging.info("My result :{}".format(result))
    return jsonify(result);

def response(status):
    order=status["order"]
    return {"order": order}