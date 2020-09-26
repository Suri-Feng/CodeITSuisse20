import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/revisitgeometry', methods=['POST'])
def evaluateGeometry():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    #inputValue = data.get("input");
    result = []
    for testCase in data:
        result.append(geometry(testCase["shapeCoordinates"], testCase["lineCoordinates"]))


    logging.info("My result :{}".format(result))
    return jsonify(result);



def geometry(x, y):
    return []